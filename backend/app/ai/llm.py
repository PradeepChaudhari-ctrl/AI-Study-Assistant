import ollama


class LLMService:
    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        prompt = f"""
You are an AI Study Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]