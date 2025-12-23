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
        """Write a product description using the following details:
        Product Name: {product_name}
        Category: {category}
        Features: {features}
        Dimensions: {dimensions}
        Price: {price}
        Release Date: {release_date}""")
])

llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini") # Initialize the LLM 
pipeline = prompt | llm # pipe symbol is chain operator

# Pass all variables during invocation
response = pipeline.invoke({
    "product_name": "LG 4KTV XYZ1232AB",
    "category": "Electronics",
    "features": "120 w sound, super clarity, dual glass, magic remote",
    "dimensions": "100x80x20cm",
    "price": "Rs.123242/-",
    "release_date": "June 2025"
})

print(response.content)
