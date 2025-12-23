from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

# Simple conversation with full history
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Multi-turn conversation
conversation.predict(input="I'm building an AI agent for lead qualification")
conversation.predict(input="What data should I collect from prospects?")
conversation.predict(input="What was my original goal again?")  # Tests memory

# View conversation history
print(memory.buffer)
