import streamlit as st
from azure_storage import AzureStorage
from openai_transcription import OpenAITranscription

azure_storage = AzureStorage()
openai_transcription = OpenAITranscription()

def transcribe():
    st.title("Audio Transcription App")
    audio_link = st.text_input("Enter the link to your audio or video file")
    if st.button("Transcribe"):
        try:
            transcription = openai_transcription.transcribe_audio_from_link(audio_link, azure_storage)
            st.write(transcription)
            with open("transcription.txt", "w") as f:
                f.write(transcription)
            st.markdown("Download Transcription [Here](transcription.txt)")
        except Exception as e:
            st.write("An error occurred: ", str(e))

transcribe()