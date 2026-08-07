import client from "../api/client";

export async function uploadDocument(file) {
  const formData = new FormData();

  formData.append("title", file.name);
  formData.append("file", file);

  const response = await client.post(
    "/documents/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}

export async function getDocuments() {
  const response = await client.get("/documents");

  return response.data;
}