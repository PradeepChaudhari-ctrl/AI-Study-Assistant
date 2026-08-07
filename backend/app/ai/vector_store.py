import faiss
import numpy as np


class VectorStore:
    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, embeddings: list[list[float]], texts: list[str]):
        vectors = np.array(embeddings, dtype="float32")

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(vectors)

        self.texts = texts

    def search(self, embedding: list[float], k: int = 3):
        query = np.array([embedding], dtype="float32")

        scores, indices = self.index.search(query, k)

        results = []

        for idx, score in zip(indices[0], scores[0]):
            results.append(
                {
                    "text": self.texts[idx],
                    "score": float(score),
                }
            )

        return results