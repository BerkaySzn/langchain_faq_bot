from langchain_community.document_loaders import TextLoader, PDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_documents(path: str):
    # Determine file type and load accordingly
    file_extension = os.path.splitext(path)[1].lower()
    
    if file_extension == '.pdf':
        loader = PDFLoader(path)
    elif file_extension == '.docx':
        loader = Docx2txtLoader(path)
    else:  # Default to text loader for .txt and other files
        loader = TextLoader(path)
    
    documents = loader.load()
    
    # Use recursive character splitter for all document types
    text_splitter = RecursiveCharacterTextSplitter(
        # Split by these characters in order of preference
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False
    )
    
    # Split documents and add metadata
    chunks = text_splitter.split_documents(documents)
    
    # Add file information to metadata
    for chunk in chunks:
        chunk.metadata.update({
            "source": path,
            "file_type": file_extension,
            "file_name": os.path.basename(path)
        })
    
    return chunks 
