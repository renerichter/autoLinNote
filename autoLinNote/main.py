import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from autoLinNote.transcribe import transcribe_audio, work_on_transcription
from autoLinNote.utils.io import get_file_list
from autoLinNote.utils.transcript import load_transformers_model_and_tokenizer


def main():
    #video_path = "data/sample_video/sample.mp4"
    file_path = "/path/to/file"
    transcript_path=""
    file_list = get_file_list(file_path)
    
    instruction =   """
                    You are the world's best teacher of system design and architecture. Please summarize the transcript into 10-15 compact bullet-points thereby focusing on the main and important concepts and facts while structuring and grouping the bullet-points to get a well structured list. Make particularly important infos bold while creating an unnumbered list. 
                    Add 3 questions for each of Bloom's taxonomy level 5, 4, and 1 (in the given order) about the transcript. Add these questions as just another main-bullet-point to the list where the top level is "QnA (according to Blooms taxonomy)", the next level marks the taxonomy grade and deepest level holds the respective questions. As last (main) bullet point create a "line to ponder", which fuels curiosity to its maximum with respect to the text summarized. 
                    Add a brief summary of 
                    Your notation style is very technical and concise. The list is continuous (meaning no additional line-breaks or left-out-lines) and uses markdown correct spacings for each bullet-point.
                    """
    transcribe_model_name = "openai/whisper-base"
    work_model_name = {'llama2':'meta-llama/Llama-2-7b-chat-hf','llama3':"meta-llama/Meta-Llama-3.1-8B",'GPTJ':'EleutherAI/gpt-j-6B'}

    transcriptions,video_names =transcribe_audio(file_list,whisper_model_name=transcribe_model_name,transcript_path=transcript_path,chunk_window_size=2,verbose=True)
    
    if False:
        model, tokenizer=load_transformers_model_and_tokenizer(model_name=work_model_name["llama3"])
        response = work_on_transcription(transcription,instruction,response_path="results/response.txt",tokenizer=tokenizer,model=model,max_tokens=250,model_max_new_tokens=150,verbose=True)
    print("nice")




if __name__=="__main__":
    main()