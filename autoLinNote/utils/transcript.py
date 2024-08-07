import os

from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          WhisperForConditionalGeneration, WhisperProcessor)


# Function to load or download and save the Whisper model
def load_model_and_processor(load_directory):
    # Check if the directory exists
    if not os.path.exists(load_directory):
        raise FileNotFoundError(f"Directory {load_directory} does not exist.")

    # Load the processor
    processor = WhisperProcessor.from_pretrained(load_directory)

    # Load the model
    model = WhisperForConditionalGeneration.from_pretrained(load_directory)

    return model, processor

def save_model_and_processor(whisper_model_name, save_directory):
    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Download and save the processor
    processor = WhisperProcessor.from_pretrained(whisper_model_name)
    processor.save_pretrained(save_directory)

    # Download and save the model
    model = WhisperForConditionalGeneration.from_pretrained(whisper_model_name)
    model.save_pretrained(save_directory)

    print(f"Model and processor saved to {save_directory}")

# Function to get the model and processor (either by loading or downloading)
def get_model_and_processor(whisper_model_name, local_directory):
    if os.path.exists(local_directory):
        print("Loading model and processor from local directory...")
    else:
        print("Downloading and saving model and processor...")
        save_model_and_processor(whisper_model_name, local_directory)
    return load_model_and_processor(local_directory)


def load_transformers_model_and_tokenizer(model_name="meta-llama/Meta-Llama-3.1-8B",local_model_path:str="",tokenizer_path:str=""):
    # make sure paths are ok
    local_model_path="data/local_model_copy/"+model_name.split("/")[-1]+"-model" if local_model_path=="" else local_model_path
    tokenizer_path=local_model_path[:-5]+"tokenizer" if tokenizer_path=="" else tokenizer_path

    # get tokenizer and model
    if os.path.exists(local_model_path) and os.path.exists(tokenizer_path):
        model = AutoModelForCausalLM.from_pretrained(local_model_path)
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        print(f"Loaded {model_name} model and tokenizer from {local_model_path} and {tokenizer_path}")
    else:
        print(f"Local model or tokenizer not found. Downloading {model_name} model and tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer.save_pretrained(tokenizer_path)
        model.save_pretrained(local_model_path)
        print(f"Saved {model_name} model and tokenizer to {local_model_path} and {tokenizer_path}")
    return model, tokenizer
