import subprocess


def extract_audio(video_path, audio_path):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-c:a", "aac",
        "-b:a", "192k",
        audio_path
    ]
    subprocess.run(command, check=True)

    print(f"Extracted audio to {audio_path}")