import streamlit as st

import whisper

st.title("Whisper App")

#upload audio 
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

@st.cache
def load_whisper_model():
    model = whisper.load_model("base")
    return model

if st.sidebar.button("Load Whisper Model"):
    model = load_whisper_model()
    st.sidebar.success("Whisper Model Loaded")

# streamlit function to get the file path 
def get_audio_file_details(file):
    file_details = {"FileName": file.name, "FileType": file.type, "FileSize": file.size}
    return file_details

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.message("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file :)")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)

