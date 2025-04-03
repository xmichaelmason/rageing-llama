import sqlite3
import struct
from typing import List

import sqlite_vec
from embedder import get_embeddings


def query_vectordb(db_path, text):
    db = sqlite3.connect(db_path)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)
    embedding = get_embeddings(text)

    rows = db.execute(
    """
      select
            id,
            type,
            path,
            description,
            distance
        from documents
        where embedding match ?
        and k = 20;
    """,
    [embedding]
    ).fetchall()

    return rows


if __name__ == "__main__":
    db_path = 'knowledge_base.db'
    text = "What is the capital of France?"
    results = query_vectordb(db_path, text)
    for row in results:
        print(row)