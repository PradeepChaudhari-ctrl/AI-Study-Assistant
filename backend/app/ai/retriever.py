from app.ai.embeddings import create_embeddings
from app.vectorstore.chroma import ChromaVectorStore


class Retriever:
    def __init__(self):
        self.store = ChromaVectorStore()

    def retrieve(
        self,
        question: str,
        document_id: int,
        k: int = 3,
    ) -> str:
        embedding = create_embeddings([question])[0]

        results = self.store.search(
            embedding=embedding,
            document_id=document_id,
            k=k,
        )

        documents = results["documents"][0]

        return "\n\n".join(documents)