from app.ai.llm import LLMService
from app.ai.retriever import Retriever


class RAGService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    def ask(
        self,
        question: str,
        document_id: int,
    ) -> str:
        context = self.retriever.retrieve(
            question=question,
            document_id=document_id,
        )

        return self.llm.generate(
            question=question,
            context=context,
        )