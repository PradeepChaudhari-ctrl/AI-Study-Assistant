import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getDocuments } from "../services/documentService";

export default function Documents() {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDocuments() {
      try {
        const data = await getDocuments();
        setDocuments(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadDocuments();
  }, []);

  if (loading) {
    return (
      <h2 className="text-2xl font-semibold">
        Loading documents...
      </h2>
    );
  }

  return (
    <div>
      <h1 className="mb-6 text-3xl font-bold">
        My Documents
      </h1>

      {documents.length === 0 ? (
        <p>No documents uploaded yet.</p>
      ) : (
        <div className="space-y-4">
          {documents.map((doc) => (
            <div
              key={doc.id}
              className="rounded-xl bg-white p-5 shadow"
            >
              <h2 className="text-xl font-semibold">
                📄 {doc.title}
              </h2>

              <p className="text-slate-500">
                {doc.filename}
              </p>

              <div className="mt-4 flex gap-3 flex-wrap">
                <Link
                  to={`/dashboard/chat/${doc.id}`}
                  className="rounded-lg bg-blue-600 px-4 py-2 text-white"
                >
                  💬 Chat
                </Link>

                <Link
                  to={`/dashboard/summary/${doc.id}`}
                  className="rounded-lg bg-green-600 px-4 py-2 text-white"
                >
                  📝 Summary
                </Link>

                <Link
                  to={`/dashboard/quiz/${doc.id}`}
                  className="rounded-lg bg-purple-600 px-4 py-2 text-white"
                >
                  ❓ Quiz
                </Link>

                <Link
                  to={`/dashboard/flashcards/${doc.id}`}
                  className="rounded-lg bg-orange-500 px-4 py-2 text-white"
                >
                  🗂 Flashcards
                </Link>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}