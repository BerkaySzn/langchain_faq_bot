from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vector_store(documents):
    # Using the correct API key format
    embeddings = OpenAIEmbeddings(
        openai_api_key="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",
        model="text-embedding-3-small"  # Specify the embedding model
    )
    
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    return vector_store