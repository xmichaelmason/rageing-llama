from dotenv import load_dotenv
import os
import sqlite3
import sqlite_vec
from indexer import index_document

load_dotenv()

db_path = os.getenv("DB_PATH")
document_path = os.getenv("DOCUMENT_PATH")

db = sqlite3.connect(db_path)
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

db.execute(
    """
        CREATE VIRTUAL TABLE IF NOT EXISTS documents using vec0(
          id INTEGER PRIMARY KEY,
          type TEXT,
          path TEXT,
          description TEXT,
          embedding float[384]
        );
    """
)

for doc in os.listdir(document_path):
    if doc.endswith((".jpg", ".jpeg", ".png")):
        index_document(db_path, os.path.join(document_path, doc))
