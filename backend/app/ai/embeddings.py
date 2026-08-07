from sentence_transformers import SentenceTransformer

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Convert text chunks into embeddings.
    """
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    return embeddings.tolist()