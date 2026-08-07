SUMMARY_PROMPT = """
You are an AI Study Assistant.

Create a well-structured summary of the following document.

Rules:
- Keep the summary between 200 and 300 words.
- Highlight the important concepts.
- Use simple and clear English.
- Return only the summary.

Document:
{context}
"""


QUIZ_PROMPT = """
You are an AI Study Assistant.

Create {count} multiple-choice questions from the following document.

Rules:
- Each question must have exactly 4 options.
- Mention the correct answer after each question.
- Return only the quiz.

Document:
{context}
"""


FLASHCARD_PROMPT = """
You are an AI Study Assistant.

Create {count} flashcards from the following document.

Rules:
- Each flashcard must contain:
  Front:
  Back:
- Front should contain a short question or concept.
- Back should contain a concise explanation.
- Return only the flashcards.

Document:
{context}
"""