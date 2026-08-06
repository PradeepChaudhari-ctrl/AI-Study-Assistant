from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.document import Document


class DocumentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_document(
        self,
        title: str,
        filename: str,
        file_path: str,
        content_type: str,
        owner_id: int,
    ) -> Document:
        document = Document(
            title=title,
            filename=filename,
            file_path=file_path,
            content_type=content_type,
            owner_id=owner_id,
        )

        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)

        return document

    async def get_documents_by_user(
        self,
        owner_id: int,
    ):
        result = await self.db.execute(
            select(Document).where(Document.owner_id == owner_id)
        )

        return result.scalars().all()