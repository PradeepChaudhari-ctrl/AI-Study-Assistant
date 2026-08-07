import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { generateSummary } from "../services/summaryService";

export default function Summary() {
  const { documentId } = useParams();

  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadSummary() {
      try {
        const result = await generateSummary(documentId);
        setSummary(result);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadSummary();
  }, [documentId]);

  if (loading) {
    return (
      <h2 className="text-2xl font-semibold">
        Generating summary...
      </h2>
    );
  }

  return (
    <div className="max-w-5xl">
      <h1 className="mb-6 text-3xl font-bold">
        📄 AI Summary
      </h1>

      <div className="rounded-xl bg-white p-6 shadow">
        <p className="whitespace-pre-wrap leading-8">
          {summary}
        </p>
      </div>
    </div>
  );
}