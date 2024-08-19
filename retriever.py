from vectorstore import vectorstore

retriever = vectorstore.as_retriever(k=2)
