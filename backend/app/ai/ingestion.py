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

        print("\n" + "=" * 60)
        print("AI INGESTION STARTED")
        print("=" * 60)
        print(f"Document ID : {document_id}")
        print(f"File Path   : {file_path}")

        # Extract text
        text = extract_text_from_pdf(file_path)

        print("\nExtracted Characters:", len(text))

        if text:
            print("\nFirst 500 Characters:\n")
            print(text[:500])
        else:
            print("\nNo text extracted from PDF!")

        if not text:
            print("\nDocument indexing stopped because text is empty.")
            return 0

        # Chunk text
        chunks = chunk_text(text)

        print(f"\nNumber of Chunks: {len(chunks)}")

        if len(chunks) > 0:
            print("\nFirst Chunk:\n")
            print(chunks[0][:500])

        if not chunks:
            print("\nChunking failed.")
            return 0

        # Create embeddings
        print("\nGenerating embeddings...")

        embeddings = create_embeddings(chunks)

        print(f"Generated {len(embeddings)} embeddings.")

        # Create IDs
        ids = [
            f"{document_id}_{i}"
            for i in range(len(chunks))
        ]

        # Metadata
        metadatas = [
            {
                "document_id": document_id,
                "owner_id": owner_id,
                "chunk": i,
            }
            for i in range(len(chunks))
        ]

        # Store in ChromaDB
        print("\nSaving to ChromaDB...")

        self.vector_store.add_documents(
            ids=ids,
            texts=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print("\nSuccessfully indexed document!")
        print(f"Indexed {len(chunks)} chunks for document {document_id}")
        print("=" * 60 + "\n")

        return len(chunks)