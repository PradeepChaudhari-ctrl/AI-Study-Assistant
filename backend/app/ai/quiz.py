from app.ai.llm import LLMService
from app.ai.prompts import QUIZ_PROMPT
from app.ai.retriever import Retriever


class QuizService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    def generate_quiz(
        self,
        document_id: int,
        count: int = 5,
    ) -> str:

        context = self.retriever.retrieve(
            question="Generate quiz from this document.",
            document_id=document_id,
            k=8,
        )

        prompt = QUIZ_PROMPT.format(
            context=context,
            count=count,
        )

        return self.llm.generate(
            question="Generate Quiz",
            context=prompt,
        )