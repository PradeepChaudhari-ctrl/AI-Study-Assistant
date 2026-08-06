from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    title: str
    filename: str
    content_type: str

    model_config = {
        "from_attributes": True
    }