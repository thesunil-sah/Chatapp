import os 
from langchain.document_loaders import PyPDFLoader

DATA_DIR = "data"

def get_pdf_text():
    all_text = ""

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            file_path =os.path.join(DATA_DIR,filename)
            loader = PyPDFLoader(file_path)
            pages = loader.lazy_load()
            for page in pages:
                all_text += page.page_content + "\n"

    return all_text