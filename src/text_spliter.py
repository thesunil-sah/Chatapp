from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
def text_spliter(raw_text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = splitter.split_text(raw_text)
   # print(chunks[0])
   # print(type(chunks))

    docs =[Document(page_content=str(chunks))for chunk in chunks]
    return docs