# Audio Transcription App


## Installation

To install the required dependencies, run the following command:

brew install ffmpeg

```bash
pip install -r requirements.txt

```
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

pip install git+https://github.com/openai/whisper.git -q
or
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

## Configuration

export OPENAI_API_KEY="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"



## Running the App

To run the app, execute the following command:

```bash
streamlit run app.py
```

## Usage

1. Open the app in your web browser.
2. If you are not logged in, you will be redirected to Google for authentication.
3. Once you are authenticated, you will be redirected back to the app.
4. Paste the link to your audio or video file in the input field and click the "Transcribe" button.
5. The app will transcribe the audio and display the transcription.
6. You can download the transcription as a .TXT file by clicking the "Download Transcription" link.

