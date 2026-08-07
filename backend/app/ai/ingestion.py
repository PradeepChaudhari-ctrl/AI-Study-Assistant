from app.ai.embeddings import create_embeddings
from app.documents.chunking import chunk_text
from app.documents.utils import extract_text_from_pdf
from app.vectorstore.chroma import ChromaVectorStore


class AIIngestionService:
    def __init__(self):
        self.vector_store = ChromaVectorStore()

    def process_document(
        self,
        document_id: int,
        file_path: str,
        owner_id: int,
    ) -> int:
        """
        Extract text, create chunks, generate embeddings,
        and store everything in ChromaDB.
        """

        text = extract_text_from_pdf(file_path)

        if not text:
            return 0

        chunks = chunk_text(text)

        if not chunks:
            return 0

        embeddings = create_embeddings(chunks)

        ids = [
            f"{document_id}_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                "document_id": document_id,
                "owner_id": owner_id,
                "chunk": i,
            }
            for i in range(len(chunks))
        ]

        self.vector_store.add_documents(
            ids=ids,
            texts=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        return len(chunks)