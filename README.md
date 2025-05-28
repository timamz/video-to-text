# Video Transcription Script

This script extracts audio from a video file and transcribes its contents to text using OpenAI's Whisper model.

## Features

* Extracts audio from a video file in `.wav` format using `ffmpeg`.
* Transcribes the audio using `whisper` (OpenAI's Whisper model).
* Saves the resulting transcription to `output.txt` on the desktop.

## Prerequisites

* Python 3.7+
* Install dependencies:

  ```bash
  pip install ffmpeg-python openai-whisper
  ```
* Ensure `ffmpeg` is installed and accessible in your system PATH.

## Usage

Run the script from the command line:

```bash
python video_to_text.py <video_file.mp4>
```

For example:

```bash
python video_to_text.py sample_video.mp4
```

This will create a file `output.txt` containing the transcription.

## Notes

* The script uses the `base` Whisper model by default. You can change the model by modifying the `model_name` parameter in the `transcribe_video` function.
* Temporary audio files are cleaned up after transcription.