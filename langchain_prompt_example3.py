from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

# Role-based prompt with template variables
prompt = ChatPromptTemplate.from_messages([
    ("system", 
        """You are a seasoned sales person, experienced in writing persuasive
         product descriptions. 
        You write compelling product descriptions for e-commerce applications."""),
    ("user", 
        """Write a product description for the {query} using the following details:
        Product Name
        Category
        Features
        Dimensions
        Price
        Release Date """)
])

llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini") # Initialize the LLM 
pipeline = prompt | llm # pipe symbol is chain operator


# let's pass some generic input and let the model figure it out
response = pipeline.invoke({
   "query": "LG 4KTV XYZ1232AB, Electronics, 120 w sound, super clarity, dual glass, magic remote, 100x80x20cm, Rs.123242/-, June 2025"
})

print(response.content)
