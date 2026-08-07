from app.ai.llm import LLMService


class AIService:
    def __init__(self):
        self.llm = LLMService()

    def generate(
        self,
        question: str,
        prompt: str,
    ) -> str:

        return self.llm.generate(
            question=question,
            context=prompt,
        )