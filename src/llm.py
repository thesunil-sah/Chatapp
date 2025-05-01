from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
def get_conversation_chain(retriever):
    llm = ChatOpenAI(
        temperature =0,
        model_name="gpt-3.5-turbo"
                     )

    memory = ConversationBufferMemory(
        memory_key="chat_history",return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
    return chain