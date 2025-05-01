from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceBgeEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv() # load all api key 

def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings =HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    vectorstore = FAISS.from_documents(text_chunks,embedding=embeddings)

    return vectorstore