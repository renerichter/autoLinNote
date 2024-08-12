# autoLinNote

## Goal

I want to switch from linear note-taking to mind-maps but want to have a set of the most relevant points, from the videos I am watching for learning, extracted from the video.

## Situation

I have the videos as offline resources and could easily just extract the voice-line, if necessary.

## Description

autoLinNote is a CLI tool that processes input videos/audio files and gives back a transcript in formatted `.md` format. It aims to assist in creating mind-maps by extracting the most relevant points from educational videos.

## Prepare VSCODE

Create `.vscode` folder and edit `launch.json` via `mkdir .vscode && cd .vscode && nano launch.json` and paste

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "HF_HOME": "your/path/to/hugginface/token" // Example environment variable
            }
        }
    ]
}
```

Save and continue. If no token exists, run `huggingface-cli login` to create one and use the path you get from there.

## Findings

* 20240808 -- HuggingFace llama-3.1-8B: stopped output-generation (for input with less then 2048 tokens) after 30min 

## ToDo

* [ ] find llama-3.1-8b inference-optimized models for M1 pro architecture
* [ ] try [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert)
* [ ] test ollama + llamafile implementation instead of not-for-inference-optimized hugginface libraries/models
* [ ] 

## License

Check the [License](./LICENSE.md) file. :)

## Support

🤩 Right now in tinkering phase and anyways open to any fun ideas. 😎
