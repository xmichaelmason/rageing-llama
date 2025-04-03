# WIP README for Rageing Llama

## Project Overview
Rageing Llama is a multimodal AI project that combines image and text processing capabilities. It leverages state-of-the-art models for generating embeddings, processing images, and indexing documents in a database for efficient retrieval and analysis.

## Features
- **Image Processing**: Uses a vision-based Llama model to generate detailed descriptions of images.
- **Text Embeddings**: Employs Sentence Transformers to create embeddings for text data.
- **Document Indexing**: Automatically indexes images and text files into a SQLite database with vector support for efficient querying.

## Project Structure
```
/home/mason/Source/rageing-llama
├── documents/                # Directory containing input documents (images, text files, etc.)
├── models/                   # Directory for storing pre-trained models
├── src/                      # Source code for the project
│   ├── embedder.py           # Handles text embedding generation
│   ├── indexer.py            # Indexes documents into the database
│   ├── main.py               # Main entry point for the project
│   ├── multimodal.py         # Processes images and integrates with the Llama model
├── requirements.txt          # Python dependencies for the project
├── knowledge_base.db         # SQLite database for storing indexed documents
```

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment variables by creating a `.env` file:
   ```
   DB_PATH=knowledge_base.db
   DOCUMENT_PATH=documents/
   HF_HUB_CACHE=models/
   HF_TOKEN=
   ```
4. Place your documents (images or text files) in the `documents/` directory.
5. Run the main script to index the documents:
   ```bash
   python src/main.py
   ```

## Usage
- **Image Processing**: The `process_image` function in `multimodal.py` generates detailed descriptions of images.
- **Text Embeddings**: The `get_embeddings` function in `embedder.py` creates embeddings for text data.
- **Document Indexing**: The `index_document` function in `indexer.py` indexes documents into the SQLite database.

## Dependencies
- Python 3.10+
- Libraries:
  - `dotenv`
  - `transformers[torch]`
  - `sentence-transformers`
  - `pillow`
  - `sqlite-vec`

## Future Work
- Add support for additional file types.
- Implement advanced querying capabilities.
- Improve the user interface for interacting with the database.

## License
This project is currently under development. Licensing details will be added in the future.