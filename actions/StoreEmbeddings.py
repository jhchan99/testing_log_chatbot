import chromadb
import uuid
from datetime import datetime


class EmbeddingStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma_db")
        self.collection = self.client.get_or_create_collection("logs")

    def add_documents(self, documents):
        metadata = {
            "source": "logs",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "user": "unknown",
            "ip": "unknown",
            "action": "unknown",
        }

        self.collection.add(
            documents=documents,
            ids=[str(uuid.uuid4()) for _ in range(len(documents))],
            metadatas=[metadata for _ in range(len(documents))],
        )

    def query(self, query, k=5):
        return self.collection.query(query_texts=[query], n_results=k)
