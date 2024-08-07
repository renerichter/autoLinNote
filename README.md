# Transcriber

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

## License

Check the [License](./LICENSE.md) file. :)

## Support

🤩 Right now in tinkering phase and anyways open to any fun ideas. 😎
