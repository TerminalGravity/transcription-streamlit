import openai
from config import OPENAI_API_KEY
from pydub import AudioSegment
import os
import tempfile

class OpenAITranscription:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def transcribe_audio(self, audio_file_path):
        # Convert audio file to wav format
        audio = AudioSegment.from_file(audio_file_path)
        wav_file_path = os.path.join(tempfile.gettempdir(), "temp.wav")
        audio.export(wav_file_path, format="wav")

        # Transcribe audio file using Whisper ASR
        with open(wav_file_path, "rb") as f:
            response = openai.WhisperASR.create(audio=f)

        # Delete temporary wav file
        os.remove(wav_file_path)

        # Return transcription
        return response['choices'][0]['text']

    def transcribe_audio_from_link(self, audio_link, azure_storage):
        # Download audio file from Azure Storage
        audio_file_path = os.path.join(tempfile.gettempdir(), "temp_audio_file")
        azure_storage.download_file(audio_link, audio_file_path)

        # Transcribe audio file
        transcription = self.transcribe_audio(audio_file_path)

        # Delete temporary audio file
        os.remove(audio_file_path)

        # Return transcription
        return transcription
