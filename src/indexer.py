import sqlite3
from multimodal import process_image
from embedder import get_embeddings


def get_file_type(file_path):
    if file_path.endswith(".txt"):
        return "text"
    elif file_path.endswith((".jpg", ".jpeg", ".png")):
        return "image"
    else:
        raise ValueError("Unsupported file type")

def index_document(db_path, document_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    file_type = get_file_type(document_path)

    existing = cursor.execute(
        """
            SELECT path FROM documents WHERE path = ?;
        """, (document_path,)
    )

    if not existing.fetchone():
        if file_type == "image":
            description = process_image(document_path, "Describe this image in detail")
            embedding = get_embeddings([description])[0]
        cursor.execute(
            """
                INSERT INTO documents (type, path, description, embedding) VALUES (?, ?, ?, ?);
            """, (file_type, document_path, description, embedding)
        )

        conn.commit()