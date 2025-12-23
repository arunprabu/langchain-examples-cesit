# Prompt Examples

## LLMs
1. Chat / Completion models
2. Reasoning-optimized models (chain-of-thought / structured reasoning)
3. Agentic models (agents, agentic coding)
4. Image generation models (text-to-image)
5. TTS / Audio generation models (text-to-speech, audio synthesis)
6. ASR (Automatic Speech Recognition) / Transcription models (speech-to-text)
7. Video generation models
8. Embedding / Semantic search models
9. Multimodal models (text + image/audio etc.)

## Gen AI Apps
- AI Chatbots / Copilots
- AI Agents
- Multi-agent systems
- AI Workflows

## 3 Ways to build Gen AI Apps
1. No-code tools (Relay, LangSmith Agent Builder [beta])
2. Low-code tools (n8n, LangFlow)
3. Full-code tools (LangChain, AutoGen, CrewAI, Agno, LlamaIndex, Vercel AI SDK)

## Languages & Frameworks
- Languages: Python, JS/TS, .NET, Java
- Frameworks:
  - LangChain (Python and JS/TS)
    - v0.1, v0.2, v0.3, v1 (released Oct 2025)
  - AutoGen (Python)
  - CrewAI (Python)
  - LlamaIndex (Python)
  - Agno AGI (Python)
  - Vercel AI SDK (JS/TS)
  - Microsoft Semantic Kernel (.NET)

## LangChain
- Prerequisite: Python

## Making LLM Output More Deterministic
Techniques:
- Few-shot prompting
- Explicitly state the expected output type
- Use structured output (e.g., JSON schema)

## LangChain Project Setup
Recommended Python version for LangChain v1 (as of 15 Dec 2025): **Python 3.13**

Commands to try:
```bash
python --version
pip --version
```

Create a virtual environment (do it once):
```bash
python -m venv .venv
```

Activate virtual environment (macOS / Linux):
```bash
source .venv/bin/activate
```

Activate virtual environment (Windows - PowerShell / CMD):
```powershell
.\.venv\Scripts\activate
```

Install LangChain packages and dotenv:
```bash
pip install -U langchain langchain-openai python-dotenv
```

## Example: Complex task decomposition using chained prompts
Here is the draft LinkedIn post you wrote:
```
[PASTE POST]
```

Tasks:
1. Critique this post for clarity, specificity, and strength of CTA.
2. Suggest 3 concrete improvements.
3. Provide a revised version that applies those improvements.

