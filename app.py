import streamlit as st
from azure_storage import AzureStorage
from openai_transcription import OpenAITranscription
from google_auth import google_auth, google_auth_callback
from flask import Flask, redirect, url_for, session
from flask import render_template
from config import APP_SECRET_KEY

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY

azure_storage = AzureStorage()
openai_transcription = OpenAITranscription()

@app.route("/")
def home():
    if 'email' not in session:
        return redirect(url_for("google_auth_route"))
    else:
        return render_template('index.html')

@app.route("/google_auth")
def google_auth_route():
    return google_auth()

@app.route("/google_auth/callback")
def google_auth_callback_route():
    return google_auth_callback()


@app.route("/transcribe")
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

if __name__ == "__main__":
    app.run(port=8501)
