from dotenv import load_dotenv
import os

load_dotenv()  

from langchain_community.llms import Ollama

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

#llm = ChatOpenAI(temperature=0.7, api_key="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")  
llm = Ollama(model="llama3")
memory = ConversationBufferMemory(return_messages=True)
chain = ConversationChain(llm=llm, memory=memory)

def init_chat_memory(summary):
    memory.clear()
    system_prompt = (
        "You are a helpful AI assistant that helps users understand video content.\n"
        "The video has already been analyzed and summarized. Use the summary to answer questions accurately.\n"
        "If the question is unrelated to the video, politely decline.\n"
        f"\nHere is the summary of the video:\n{summary}"

        
    )
    chain.predict(input=system_prompt)
def handle_chat(user_input, summary_cache=None):
    return chain.predict(input=user_input)


