from app.ai.llm import LLMService
from app.ai.prompts import FLASHCARD_PROMPT
from app.ai.retriever import Retriever


class FlashcardService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    def generate_flashcards(
        self,
        document_id: int,
        count: int = 10,
    ) -> str:

        context = self.retriever.retrieve(
            question="Generate flashcards from this document.",
            document_id=document_id,
            k=8,
        )

        prompt = FLASHCARD_PROMPT.format(
            context=context,
            count=count,
        )

        return self.llm.generate(
            question="Generate Flashcards",
            context=prompt,
        )