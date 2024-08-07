import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from autoLinNote.transcribe import transcribe_audio, work_on_transcription
from autoLinNote.utils.transcript import load_transformers_model_and_tokenizer


def main():
    #video_path = "data/sample_video/2.1  Introduction to System Design & Architectural Direct Drivers [479wrNwaiSE].mp4"
    video_path = audio_path = "data/sample_audio/2.1_test.m4a"
    instruction =   """
                    You are the world's best teacher of system design and architecture. Please summarize the transcript into 15 bullet-points thereby focusing on the main and important concepts and facts. Make particularly important infos bold. Finally, add 3 questions for each of Bloom's taxonomy level 1, 4, and 5 about the transcript.
                    """
    transcribe_model_name = "openai/whisper-base"
    work_model_name = {'llama2':'meta-llama/Llama-2-7b-chat-hf','llama3':"meta-llama/Meta-Llama-3.1-8B",'GPTJ':'EleutherAI/gpt-j-6B'}

    transcription,video_name =transcribe_audio(video_path,audio_path,whisper_model_name=transcribe_model_name,transcript_path="results/transcript.txt",verbose=True)
    model, tokenizer=load_transformers_model_and_tokenizer(model_name=work_model_name["llama3"])
    response = work_on_transcription(transcription,instruction,response_path="results/response.txt",tokenizer=tokenizer,model=model,verbose=True)
    print("nice")




if __name__=="__main__":
    main()