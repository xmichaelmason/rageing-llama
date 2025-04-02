
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

sentences = ["This is an example sentence", "Each sentence is converted"]


def get_embeddings(sentences) -> list:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings

if __name__ == "__main__":
    # Example usage
    sentences = ["This is an example sentence", "Each sentence is converted"]
    embeddings = get_embeddings(sentences)
    print(embeddings)
