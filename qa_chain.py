from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

def create_qa_chain(vector_store):
    # Create the language model
    llm = ChatOpenAI(
        openai_api_key="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",
        model="gpt-3.5-turbo"
    )
    
    # Create a simple chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    
    return chain
