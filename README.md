# Audio Transcription App

This is a simple, single page app that transcribes an audio file using the Whisper ASR model from OpenAI. The app is scripted in Python and hosted on Streamlit. It uses Azure for temporary data storage, Google OAuth for ADR, and allows users to paste a link to a video or audio file. The app will then transcribe the audio, showing the completion progress and relevant file details. The output is a .TXT file of the transcription, which can be downloaded via a link.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the app, you need to set up the following environment variables in a `.env` file:

- `AZURE_STORAGE_CONNECTION_STRING`: Your Azure Storage connection string
- `AZURE_STORAGE_CONTAINER_NAME`: Your Azure Storage container name
- `OPENAI_API_KEY`: Your OpenAI API key
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
- `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret
- `GOOGLE_REDIRECT_URI`: Your Google OAuth redirect URI
- `APP_SECRET_KEY`: Your app secret key

You can set these variables by creating a `.env` file in the root directory of the project and adding the variables like this:

```bash
AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
AZURE_STORAGE_CONTAINER_NAME=your_azure_storage_container_name
OPENAI_API_KEY=your_openai_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=your_google_redirect_uri
APP_SECRET_KEY=your_app_secret_key
```

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

