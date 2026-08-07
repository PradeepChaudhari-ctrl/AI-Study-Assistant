import { useState } from "react";
import { useParams } from "react-router-dom";

import { askQuestion } from "../services/chatService";

export default function Chat() {
  const { id } = useParams();

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend() {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const result = await askQuestion(id, question);

      const aiMessage = {
        role: "assistant",
        text: result.answer,
      };

      setMessages((prev) => [...prev, aiMessage]);

      setQuestion("");
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Something went wrong.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-5xl mx-auto">

      <h1 className="text-3xl font-bold mb-6">
        AI Chat
      </h1>

      <div className="bg-white rounded-xl shadow p-6">

        <div className="h-[500px] overflow-y-auto border rounded-lg p-4 mb-5">

          {messages.length === 0 && (
            <p className="text-slate-400">
              Ask anything about your document...
            </p>
          )}

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`mb-4 ${
                msg.role === "user"
                  ? "text-right"
                  : "text-left"
              }`}
            >
              <div
                className={`inline-block rounded-xl px-4 py-3 ${
                  msg.role === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-gray-100"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}

        </div>

        <div className="flex gap-3">

          <input
            className="flex-1 border rounded-lg px-4 py-3"
            placeholder="Ask anything..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSend();
              }
            }}
          />

          <button
            onClick={handleSend}
            disabled={loading}
            className="bg-blue-600 text-white px-6 rounded-lg"
          >
            {loading ? "..." : "Send"}
          </button>

        </div>

      </div>

    </div>
  );
}