from os import makedirs, path, remove
from typing import List, Tuple

import librosa
import torch

from autoLinNote.utils.audio import extract_audio
from autoLinNote.utils.transcript import get_model_and_processor

# Function to extract audio from video using ffmpeg

def load_transcript(transcript_path):
    with open(transcript_path,"r",encoding="utf-8") as f:
        transcript = f.read()
    return transcript

# Extract audio
def transcribe_audio(file_paths:list=[],whisper_model_name:str="openai/whisper-base",whisper_path:str="",transcript_path:str="",sampling_rate:int=16000,chunk_window_size:int=5,delete_video:bool=False,verbose:bool=False)->Tuple[List,list]:
    chunk_size_sec_max=30
    chunk_size_sec = chunk_size_sec_max-chunk_window_size
    transcriptions = []
    transcriptions_paths = []
    for i,afile in enumerate(file_paths):
        try:
            # make sure paths are proper
            file_name_in_path_split=    afile.split("/")
            file_name_in =              ".".join(file_name_in_path_split[-1].split(".")[:-1])
            file_name_in_type =         file_name_in_path_split[-1].split(".")[-1]
            file_name_out =             file_name_in+".m4a"
            file_path_out_proto =       path.join("/".join(file_name_in_path_split[:-2]),"audio")
            file_path_out =             path.join(file_path_out_proto,file_name_out)
            
            # make audio if necessary
            if not (file_name_in_type == "m4a" or path.exists(file_path_out)):
                makedirs(file_path_out_proto,exist_ok=True)
                
                
                extract_audio(afile,file_path_out)
                if delete_video: remove(afile)

            
            whisper_path = f"data/local_model_copy/{whisper_model_name.split('/')[-1]}" if whisper_path=="" else whisper_path
            transcript_path = f"results/{file_name_in}.txt" if transcript_path == "" else transcript_path
            transcriptions_paths.append(transcript_path)

            # Transcribe audio
            if path.exists(transcript_path):
                transcriptions.append(load_transcript(transcript_path))
            else:
                # Load the Whisper model and processor
                model, processor= get_model_and_processor(whisper_model_name, whisper_path)

                # Load the audio file
                audio, sr = librosa.load(file_path_out, sr=sampling_rate)

                # Process the audio -> whisper can only process 30s long audio
                from math import ceil
                nbr_chunks = ceil(len(audio)/sr/chunk_size_sec)
                transcribed_chunks = []
                for c in range(nbr_chunks):
                    if c==0:
                        end=chunk_size_sec_max
                        audio_sample = audio[:end*sr]
                    if c>0 and c<nbr_chunks-1:
                        start=c*chunk_size_sec
                        end=c*chunk_size_sec+chunk_size_sec_max
                        audio_sample = audio[start*sr:end*sr]
                    if c == nbr_chunks-1:
                        start=c*chunk_size_sec
                        audio_sample = audio[start*sr:]
                    input_features = processor(audio_sample, sampling_rate=sr, return_tensors="pt").input_features
                    with torch.no_grad():
                        generated_ids = model.generate(input_features)

                    # Decode the generated ids to text
                    transcribed_chunks.append(processor.batch_decode(generated_ids, skip_special_tokens=True)[0])
                    
                # Generate the transcription
                transcriptions.append("\n".join(transcribed_chunks))
                #store
                with open(transcript_path,'w',encoding="utf-8") as f:
                    f.write(transcriptions[-1])
            
            transcript_path=""
            if verbose: print(f"Transcription {i}: {transcriptions[-1]}")
            
        except Exception as e: 
            print(f"<----------   Exception was raised   ---------->\n\n{e}\n\n")

    return transcriptions,transcriptions_paths

def limited_tokenization(prompt,tokenizer,max_tokens=2048):
    inputs = tokenizer(prompt, return_tensors="pt")
    # Get the number of tokens
    num_tokens = len(inputs.input_ids[0])
    if num_tokens > max_tokens:

        # Inform the user
        print(f"The input is too long by {num_tokens - max_tokens} tokens. Please shorten it or let us truncate it for you.")
        
        # Optionally truncate the input
        inputs = tokenizer(prompt, return_tensors="pt", max_length=max_tokens, truncation=True)
    
    return inputs

# Summarize transcription
def work_on_transcription(transcription,instruction,response_path,tokenizer,model,max_tokens=2048,model_max_new_tokens=1000,verbose=False):
    
    prompt = f"""#Transcript:\n{instruction}\n\n#Transcript:\n{transcription}\n\nResponse:"""
    
    inputs = limited_tokenization(prompt,tokenizer,max_tokens)
    outputs = model.generate(**inputs, max_new_tokens=model_max_new_tokens)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if verbose: print(f"Summary: {response}")
    with open(response_path,'w',encoding="utf-8") as f:
        f.write(transcription)
    return response
