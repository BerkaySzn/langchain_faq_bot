from langchain.document_loaders import TextLoader # Load text documents from a path
from langchain.text_splitter import CharacterTextSplitter # Split texts into chunks

def load_documents(path: str): #Takes the path of our document
    loader = TextLoader(path) 
    documents = loader.load() # documents = TextLoader(path).load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents) 
