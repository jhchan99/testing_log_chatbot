import chromadb
import os
import uuid


class EmbeddingStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma_db")
        self.collection = self.client.get_or_create_collection("logs")

    def add_documents(self, documents):
        # TODO: Add more metadata
        # date, time, user, ip, action, etc.
        metadata = {"source": "logs"}
        self.collection.add(
            documents=documents,
            ids=[str(uuid.uuid4()) for _ in range(len(documents))],
            metadatas=[metadata for _ in range(len(documents))],
        )

    def query(self, query, k=5):
        return self.collection.query(query_texts=[query], n_results=k)
