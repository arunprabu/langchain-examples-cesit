
LLMs
===
  1. Chat Models / Completion Models 
  2. Reasoning Models (RECOMMENDED FOR GEN AI APPS)
  3. Agentic Coding Models 
  4. Image Generation Models 
  5. Audio Generation Models 
  6. Video Generation Models 
  7. Transcription Generator Models 



Gen AI Apps 
===
  
  1. AI Chatbots / Copilots
  2. AI Agents 
  3. Multi-agent system 
  4. AI Workflows 


3 Ways to build Gen AI Apps 
===
  #1 No Code Tools (relay, langsmith agent builder [beta] )
  #2 Low Code Tools (n8n, langflow )
  #3 Full Code Tools (langchain / autogen/crewai/agno/llamaindex/vercel ai sdk)
  

Languages
===
  Python, JS / TS, DotNet, Java
  
  Frameworks: 
    #1 LangChain (Python and JS/TS)
        v 0.1 
        v 0.2 
        v 0.3
        v 1 (released in oct 2025)

    #2 Autogen (Python)
    #3 CrewAI (Python)
    #4 LlamaIndex(Python)
    #5 Agno AGI (Python)
    #6 Vercel AI SDK (JS/TS)
    #7 MS Semantic Kernel (DotNet)

=====


LangChain 
===
  Prereq: Python 

  


How to make non-deterministic output of LLM to deterministic?
=====
  apply various technique
    Few shot Prompting 
    mention what type output you want
    structured output 
    



Langchain Project 
====
  Step 1: create a project directory. in command prompt try the following  
      mkdir prompt_examples
      cd prompt_examples

  Step 2: create venv 
    python -m venv .venv

  Step 3: Activate the venv 
    .\venv\Scripts\activate

  Step 4: start developing the examples using langchain 
    









# Complex task decomposition using chained prompts - Example Prompt
Here is the draft LinkedIn post you wrote:
[PASTE POST]

Critique this post for clarity, specificity, and strength of CTA.

Suggest 3 concrete improvements.

Then give me a revised version that applies those improvements.

======
