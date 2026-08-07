import chromadb
from chromadb.config import Settings


class ChromaVectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="chroma_db",
            settings=Settings(anonymized_telemetry=False),
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(
        self,
        ids: list[str],
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ):
        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def search(
        self,
        embedding: list[float],
        document_id: int,
        k: int = 3,
    ):
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k,
            where={
                "document_id": document_id,
            },
        )

        return results