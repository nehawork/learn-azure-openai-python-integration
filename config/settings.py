import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

api_key = os.getenv('AZURE_OPENAI_API_KEY')
api_version = os.getenv('AZURE_OPENAI_API_VERSION')
api_url = os.getenv('AZURE_OPENAI_URL')
model_name = os.getenv('AZURE_OPENAI_MODEL_NAME')

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=api_url,
    api_key=api_key,
)

__all__ = ["client", "model_name"]
