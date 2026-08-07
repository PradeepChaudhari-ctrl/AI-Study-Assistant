import client from "../api/client";

export async function generateSummary(documentId) {
  const response = await client.post("/summary", {
    document_id: Number(documentId),
  });

  return response.data.summary;
}