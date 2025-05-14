from langchain_community.document_loaders import TextLoader, Docx2txtLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

#This function load_documents(path):

    #Loads a document file (.pdf, .docx, or .txt)

    #Splits its content into manageable chunks

    #Adds metadata to each chunk

    #Returns a list of text chunks


def load_documents(path: str):

    file_extension = os.path.splitext(path)[1].lower() #'data/file.csv' → ('data/file', '.csv')
    
    if file_extension == '.pdf':
        loader = PyPDFLoader(path)
    elif file_extension == '.docx':
        loader = Docx2txtLoader(path)
    else:  # Default to text loader for .txt and other files
        loader = TextLoader(path)
    
    documents = loader.load() #Reads the document and returns it in a format that LangChain can work with.
    
    # LangChain needs your documents in a specific format (its own Document objects). 
    # These loaders abstract away the format differences so you can work with any document type seamlessly.


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
