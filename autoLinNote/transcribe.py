from os import path

import librosa
import torch

from autoLinNote.utils.transcript import get_model_and_processor

# Function to extract audio from video using ffmpeg

def load_transcript(transcript_path):
    with open(transcript_path,"r",encoding="utf-8") as f:
        transcript = f.read()
    return transcript

# Extract audio
def transcribe_audio(video_path:str,audio_path:str="",whisper_model_name:str="openai/whisper-base",whisper_path:str="",transcript_path:str="",verbose=False):
    # make sure paths are proper
    video_name = (video_path.split("/")[-1]).split(".")[:-1]
    audio_path = "".join(video_path.split(".")[:-1])+".m4a" if audio_path == "" else audio_path
    whisper_path = f"data/local_model_copy/{whisper_model_name.split("/")[-1]}" if whisper_path=="" else whisper_path
    transcript_path = f"../results/{video_name}.txt" if transcript_path == "" else transcript_path

    # Transcribe audio
    if path.exists(transcript_path):
        transcription = load_transcript(transcript_path)
    else:
        # Load the Whisper model and processor
        model, processor= get_model_and_processor(whisper_model_name, whisper_path)

        # Load the audio file
        audio, sr = librosa.load(audio_path, sr=16000)

        # Process the audio
        input_features = processor(audio, sampling_rate=sr, return_tensors="pt").input_features

        # Generate the transcription
        with torch.no_grad():
            generated_ids = model.generate(input_features)

        # Decode the generated ids to text
        transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        #store
        with open(transcript_path,'w',encoding="utf-8") as f:
            f.write(transcription)
    
    if verbose: print(f"Transcription: {transcription}")
    return transcription,video_name

# Summarize transcription
def work_on_transcription(transcription,instruction,response_path,tokenizer,model,verbose=False):
    
    prompt = f"""#Transcript:\n{instruction}\n\n#Transcript:\n{transcription}\n\nResponse:"""
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=2048, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=1000)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if verbose: print(f"Summary: {response}")
    with open(response_path,'w',encoding="utf-8") as f:
        f.write(transcription)
    return response
