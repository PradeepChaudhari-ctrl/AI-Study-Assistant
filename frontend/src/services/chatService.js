import client from "../api/client";

export async function askQuestion(documentId, question) {
  const response = await client.post("/chat", {
    document_id: Number(documentId),
    question,
  });

  return response.data;
}