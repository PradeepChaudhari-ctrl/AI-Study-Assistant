from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database.models.user import User
from app.database.session import get_db
from app.documents.repository import DocumentRepository
from app.documents.schemas import DocumentResponse
from app.documents.service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload", response_model=DocumentResponse)
async def upload_document(
    title: str = Form(...),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = DocumentService(DocumentRepository(db))

    return await service.upload_document(
        title=title,
        file=file,
        owner_id=current_user.id,
    )


@router.get("/", response_model=list[DocumentResponse])
async def list_documents(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = DocumentRepository(db)

    return await repository.get_documents_by_user(current_user.id)