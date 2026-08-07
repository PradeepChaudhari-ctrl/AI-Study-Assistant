from pydantic import BaseModel


# ---------------- CHAT ----------------

class ChatRequest(BaseModel):
    document_id: int
    question: str


class ChatResponse(BaseModel):
    answer: str


# ---------------- SUMMARY ----------------

class SummaryRequest(BaseModel):
    document_id: int


class SummaryResponse(BaseModel):
    summary: str


# ---------------- QUIZ ----------------

class QuizRequest(BaseModel):
    document_id: int
    count: int = 5


class QuizResponse(BaseModel):
    quiz: str


# ---------------- FLASHCARDS ----------------

class FlashcardRequest(BaseModel):
    document_id: int
    count: int = 10


class FlashcardResponse(BaseModel):
    flashcards: str