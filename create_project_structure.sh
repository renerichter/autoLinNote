#!/bin/zsh

# How to use this file? --------------------------------
# 1) change to liking/need
# 2) make runable chmod +x create_project_structure.zsh
# 3) run: ./create_project_structure.zsh
# ------------------------------------------------------


# Define base path
project_name="autoLinNote"
current_dir="$(dirname "$(realpath "$0")")" 
base_path="$current_dir/$project_name"

# Define directories to create
directories=(
    "$base_path"
    "$base_path/$project_name"
    "$base_path/$project_name/utils"
    "$base_path/$project_name/models"
    "$base_path/tests"
    "$base_path/data/sample_audio"
    "$base_path/data/sample_video"
    "$base_path/docs"
    "$base_path/scripts"
)

# Define files to create
files=(
    "$base_path/$project_name/__init__.py"
    "$base_path/$project_name/main.py"
    "$base_path/$project_name/cli.py"
    "$base_path/$project_name/transcribe.py"
    "$base_path/$project_name/utils/__init__.py"
    "$base_path/$project_name/utils/file_utils.py"
    "$base_path/$project_name/utils/audio_utils.py"
    "$base_path/$project_name/models/__init__.py"
    "$base_path/$project_name/models/transcript.py"
    "$base_path/$project_name/models/audio.py"
    "$base_path/tests/__init__.py"
    "$base_path/tests/test_transcribe.py"
    "$base_path/tests/test_file_utils.py"
    "$base_path/tests/test_audio_utils.py"
    "$base_path/docs/usage.md"
    "$base_path/scripts/setup_env.sh"
    "$base_path/.gitignore"
    "$base_path/README.md"
    "$base_path/requirements.txt"
    "$base_path/setup.py"
)

echo "Creating Project Structure for Project $project_name."

# Create directories
for dir in $directories; do
    mkdir -p $dir
    echo "Created directory: $dir"
done

# Create files
for file in $files; do
    touch $file
    echo "Created file: $file"
done

# prefill some files
echo "# Custom -- Ignore data folder\ndata/\n\n# Standard Python .gitignore template\n__pycache__/\n*.py[cod]\n*$py.class\n*.so\n*.egg\n*.egg-info\n.eggs/\n*.pyo\n*.pyd\n*.whl\n*.manifest\n*.spec\n*.db\n*.log\n*.sqlite3\n*.stackdump\n.coverage\n*.cover\n.hypothesis/\n*.mo\n*.pot\n*.py,cover\n.tox/\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\n*.dll\n*.dylib\n*.exe\n*.o\n*.obj\n*.pyc" > $base_path/.gitignore

echo "# autoLinNote\n\n## Goal\n\nI want to switch from linear note-taking to mind-maps but want to have a set of the most relevant points, from the videos I am watching for learning, extracted from the video.\n\n## Situation\n\nI have the videos as offline resources and could easily just extract the voice-line, if necessary.\n\n## Description\n\nTranscriber is a CLI tool that processes input videos/audio files and gives back a transcript in formatted \`.md\` format. It aims to assist in creating mind-maps by extracting the most relevant points from educational videos." > $base_path/README.md


echo "Project structure created successfully!"
