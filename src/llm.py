from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()
def get_conversation_chain(retriever):
    # llm = ChatOpenAI(
    #     temperature =0,
    #     model_name="gpt-3.5-turbo"
    #                  )
    
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})


    memory = ConversationBufferMemory(
        memory_key="chat_history",return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
    return chain