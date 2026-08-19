# MultiDocument AI

A Streamlit retrieval prototype for asking questions about PDF, DOCX, PPTX, and XLSX files.

> Status: prototype. The application is suitable for local exploration, not for confidential documents or production deployment.

## What it demonstrates

- Text extraction across four common document formats
- Character-based chunking
- OpenAI embeddings
- In-memory FAISS retrieval
- LangChain conversational retrieval
- Streamlit file upload and chat history
- User-supplied API credentials through the interface

## Flow

```mermaid
flowchart LR
    A[Uploaded document] --> B[Format-specific text extraction]
    B --> C[Text chunks]
    C --> D[OpenAI embeddings]
    D --> E[FAISS index]
    E --> F[Conversational retrieval chain]
    F --> G[Streamlit answer and chat history]
```

## Supported formats

| Format | Reader |
| --- | --- |
| PDF | PyPDF2 |
| DOCX | python-docx |
| PPTX | python-pptx |
| XLSX | pandas and openpyxl |

## Local setup

```bash
git clone https://github.com/anishmahapatra/MultiDocument-AI.git
cd MultiDocument-AI
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local Streamlit URL, enter an OpenAI API key in the sidebar, upload a supported document, and submit a question.

## Repository layout

```text
app.py             Streamlit interface and session flow
functions.py       Extraction, chunking, retrieval, and conversation helpers
htmlTemplates.py   Retained interface templates
Flowchart.png      Original architecture illustration
Showcase/          Screenshots and demo assets
archive/           Earlier implementation material
```

## Current behavior

- Each uploaded file is processed independently.
- When several files are uploaded, the final processed file becomes the active conversation chain.
- Chat history is stored in the Streamlit session.
- The FAISS index is created in process and is not persisted by the application.
- The interface returns answers without structured source citations.

## Security and privacy

Uploaded content and text chunks are sent to OpenAI for embedding and answer generation. Do not use confidential or regulated documents without reviewing provider policies and adding suitable controls.

A production version should add:

- Authentication and per-user isolation
- File size and type validation
- Malware scanning
- Explicit retention and deletion behavior
- Secret management outside the page
- Source citations and retrieval diagnostics
- Request limits, audit logs, and tests

## Known limitations

- The LangChain imports use an older package layout and should be upgraded before further development.
- There are no automated tests.
- Error handling is minimal.
- Multi-file retrieval is not implemented as a combined index.
- Model choice, chunking, and retrieval parameters are fixed in code.
