import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure Storage
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_STORAGE_CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Google OAuth
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

# App
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
