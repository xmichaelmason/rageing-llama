import sqlite3

import sqlite_vec
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
    db = sqlite3.connect(db_path)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)
    file_type = get_file_type(document_path)

    # # get row count
    # rows = cursor.execute(
    #     """
    #         SELECT COUNT(id) FROM documents;
    #     """
    # )

    # if rows is not None:
    #     existing = cursor.execute(
    #         """
    #             SELECT path FROM documents WHERE path = ?;
    #         """, (document_path,)
    #     )

    # if not existing.fetchone():
    if file_type == "image":
        description = process_image(document_path, "Describe this image in detail")
        embedding = get_embeddings([description])[0]
        db.execute(
            """
                INSERT INTO documents (type, path, description, embedding) VALUES (?, ?, ?, ?);
            """, (file_type, document_path, description, embedding)
        )

        db.commit()