import os
import ffmpeg   # now from ffmpeg-python
import whisper

def extract_audio(video_path, audio_path):
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
        .overwrite_output()
        .run(quiet=True)
    )

def transcribe_video(video_path, model_name='base'):
    temp = 'temp.wav'
    try:
        extract_audio(video_path, temp)
        model = whisper.load_model(model_name)
        result = model.transcribe(temp)
        return result['text']
    finally:
        if os.path.exists(temp):
            os.remove(temp)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <video.mp4>")
        sys.exit(1)
    # Transcribe and save to output.txt
    transcript = transcribe_video(sys.argv[1])
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(transcript)
    print("Transcript saved to output.txt")
