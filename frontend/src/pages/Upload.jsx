import { useState } from "react";
import toast from "react-hot-toast";

import Button from "../components/Button";
import { uploadDocument } from "../services/documentService";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleUpload() {
    if (!file) {
      toast.error("Please select a PDF file.");
      return;
    }

    if (file.type !== "application/pdf") {
      toast.error("Only PDF files are allowed.");
      return;
    }

    try {
      setLoading(true);

    const result = await uploadDocument(file);

console.log("UPLOAD RESPONSE:", result);

      toast.success("PDF uploaded successfully!");

      setFile(null);

      const input = document.getElementById("pdf-input");
      if (input) input.value = "";
    } catch (error) {
      console.error(error);

      toast.error(
        error.response?.data?.detail || "Upload failed"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-xl rounded-2xl bg-white p-8 shadow-lg">
      <h1 className="mb-2 text-3xl font-bold">
        Upload PDF
      </h1>

      <p className="mb-6 text-slate-500">
        Upload a PDF to chat with AI.
      </p>

      <input
        id="pdf-input"
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-6 w-full"
      />

      <Button
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Uploading..." : "Upload PDF"}
      </Button>
    </div>
  );
}