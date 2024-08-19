from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="./chroma_db_math", embedding_function=embedding_function)
