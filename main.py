from load_docs import load_documents
from vector_store import create_vector_store
from qa_chain import create_qa_chain






docs = load_documents("data/test_content.txt")
vector_store = create_vector_store(docs)

qa_chain = create_qa_chain(vector_store)

# Interactive question answering
while True:
    question = input("\nAsk a question (or type 'quit' to exit): ")
    if question.lower() == 'quit':
        break
        
    answer = qa_chain.invoke({"query": question})
    print("\nAnswer:", answer["result"])

