from app.ai.llm import LLMService
from app.ai.prompts import SUMMARY_PROMPT
from app.ai.retriever import Retriever


class SummaryService:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    def summarize(self, document_id: int) -> str:
        context = self.retriever.retrieve(
            question="Summarize this document",
            document_id=document_id,
            k=8,
        )

        prompt = SUMMARY_PROMPT.format(
            context=context,
        )

        return self.llm.generate(
            question="Summarize this document",
            context=prompt,
        )