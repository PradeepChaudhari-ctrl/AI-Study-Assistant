import os
import uuid

import aiofiles
from fastapi import UploadFile

from app.ai.ingestion import AIIngestionService
from app.documents.repository import DocumentRepository

UPLOAD_DIR = "uploads"


class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository
        self.ingestion = AIIngestionService()

    async def upload_document(
        self,
        title: str,
        file: UploadFile,
        owner_id: int,
    ):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        extension = os.path.splitext(file.filename)[1]
        filename = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(UPLOAD_DIR, filename)

        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)

        document = await self.repository.create_document(
            title=title,
            filename=file.filename,
            file_path=file_path,
            content_type=file.content_type,
            owner_id=owner_id,
        )

        chunks = self.ingestion.process_document(
            document_id=document.id,
            file_path=file_path,
            owner_id=owner_id,
        )

        print(f"Indexed {chunks} chunks for document {document.id}")

        return document