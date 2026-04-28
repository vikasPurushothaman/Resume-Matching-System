import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from config import *
from utils import extract_metadata

def load_resumes(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            docs = loader.load()

            for d in docs:
                d.metadata["source"] = file

            documents.extend(docs)

    return documents


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


def enrich_with_metadata(chunks):
    enriched_docs = []

    for doc in chunks:
        metadata = extract_metadata(doc.page_content)
        doc.metadata.update(metadata)
        enriched_docs.append(doc)

    return enriched_docs


def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    vectordb = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    vectordb.persist()
    return vectordb


if __name__ == "__main__":
    resumes_path = "./data/resumes"

    docs = load_resumes(resumes_path)
    chunks = chunk_documents(docs)
    enriched = enrich_with_metadata(chunks)

    vectordb = create_vector_store(enriched)

    print("Vector DB created successfully!")