import os
# pip install -qU langchain "langchain[openai]"
from langchain.agents import create_agent
# let's load the environment variables from a .env file
# pip install -q python-dotenv
from dotenv import load_dotenv
load_dotenv()

story_writer_agent = create_agent(
    model="gpt-4o-mini",    # brain of the agent
    system_prompt="You are a helpful assistant that writes only stories. get the {title} from the user",   #role of the agent
)

response = story_writer_agent.invoke(
  {
    "messages": [
      {
        "role": "user", 
        "content": "Write a short story in 50 words"
      }
    ]
  }
)

# let's print the last message from the response
print(response["messages"][-1].content)

