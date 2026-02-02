from qdrant_client import QdrantClient
from qdrant_client.http import models
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

class VectorDB:
    def __init__(self):
        if QDRANT_URL:
            self.client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
            print(f"Connected to Qdrant at {QDRANT_URL}")
        else:
            # Local memory fallback for dev
            print("WARNING: QDRANT_URL not set, using in-memory Qdrant")
            self.client = QdrantClient(":memory:")

    def create_collection(self, collection_name: str, vector_size: int = 1536):
        """Create a collection if it doesn't exist"""
        if not self.client.collection_exists(collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE
                )
            )
            print(f"Collection '{collection_name}' created.")
        else:
            print(f"Collection '{collection_name}' already exists.")

    def search(self, collection_name: str, query_vector: list, limit: int = 5):
        return self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit
        )

# Singleton instance
vector_db = VectorDB()
