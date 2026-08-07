from fastapi import APIRouter, HTTPException

from app.ai.rag import RAGService
from app.ai.summary import SummaryService
from app.ai.quiz import QuizService
from app.ai.flashcards import FlashcardService

from app.ai.schemas import (
    ChatRequest,
    ChatResponse,
    SummaryRequest,
    SummaryResponse,
    QuizRequest,
    QuizResponse,
    FlashcardRequest,
    FlashcardResponse,
)

router = APIRouter(
    tags=["AI"],
)

rag = RAGService()
summary_service = SummaryService()
quiz_service = QuizService()
flashcard_service = FlashcardService()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):
    try:
        answer = rag.ask(
            question=request.question,
            document_id=request.document_id,
        )

        return ChatResponse(answer=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/summary",
    response_model=SummaryResponse,
)
async def summarize(request: SummaryRequest):
    try:
        summary = summary_service.summarize(
            document_id=request.document_id,
        )

        return SummaryResponse(summary=summary)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/quiz",
    response_model=QuizResponse,
)
async def generate_quiz(request: QuizRequest):
    try:
        quiz = quiz_service.generate_quiz(
            document_id=request.document_id,
            count=request.count,
        )

        return QuizResponse(quiz=quiz)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/flashcards",
    response_model=FlashcardResponse,
)
async def generate_flashcards(request: FlashcardRequest):
    try:
        flashcards = flashcard_service.generate_flashcards(
            document_id=request.document_id,
            count=request.count,
        )

        return FlashcardResponse(
            flashcards=flashcards,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )