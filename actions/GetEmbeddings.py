import openai
import os
from dotenv import load_dotenv

load_dotenv()

class GetEmbeddings:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_embeddings(self, text):
        return self.openai_client.embeddings.create(input=text, model="text-embedding-3-small")