import uuid
from azure.storage.blob import BlobServiceClient
from config import AZURE_STORAGE_CONNECTION_STRING, AZURE_STORAGE_CONTAINER_NAME
from azure.identity import DefaultAzureCredential

class AzureStorage:
    def __init__(self):
        credential = DefaultAzureCredential()
        self.blob_service_client = BlobServiceClient(account_url="https://testblobeastusjack.blob.core.windows.net", credential=credential)
        self.container_client = self.blob_service_client.get_container_client(AZURE_STORAGE_CONTAINER_NAME)

class AzureStorage:
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        self.container_client = self.blob_service_client.get_container_client(AZURE_STORAGE_CONTAINER_NAME)

    def upload_file(self, file_path):
        blob_name = str(uuid.uuid4())
        with open(file_path, "rb") as data:
            self.container_client.upload_blob(name=blob_name, data=data)

    def download_file(self, blob_name, download_path):
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

    def delete_file(self, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
