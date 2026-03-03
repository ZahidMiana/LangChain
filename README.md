# LangChain Learning Repository

## Overview
Is repository mein LangChain ke basics aur fundamental components ko implement kiya gaya hai.

## Completed Components ✅

### 1. LLMs (Large Language Models)
- **Location:** `1.LLMS/`
- Google Gemini integration using `langchain-google-genai`
- Model: `gemini-2.5-flash` (Free tier)
- Basic text generation aur question-answering

### 2. Chat Models
- **Location:** `2.ChatModels/`
- ChatGoogleGenerativeAI implementation
- Conversational AI models
- Temperature aur parameter tuning

### 3. Embeddings
- **Location:** `3.Embeddings/`
- HuggingFace Embeddings locally
- Model: `sentence-transformers/all-MiniLM-L6-v2`
- 384-dimensional embeddings
- Text ko vector representation mein convert karna

## Environment Setup

### Required Packages
```bash
pip install -r requirements.txt
```

### API Keys Required
`.env` file mein ye API keys set karein:
```
GOOGLE_API_KEY="your_google_api_key"
GEMINI_API_KEY="your_gemini_api_key"
HUGGINGFACEHUB_API_TOKEN="your_hf_token"
```

## Project Structure
```
langchain/
├── 1.LLMS/
│   ├── llm_demo.py
│   └── test_models.py
├── 2.ChatModels/
│   ├── chatmodel4.py
│   └── chatmodel5.py
├── 3.Embeddings/
│   └── embedding2.py
├── requirements.txt
├── .env
└── README.md
```

## Next Steps 🚀
Aage aur LangChain components add kiye jayenge:
- Prompts & Prompt Templates
- Chains
- Memory
- Agents
- Vector Stores
- Document Loaders
- Retrievers

## Technologies Used
- **LangChain** - LLM framework
- **Google Gemini** - AI model (free tier)
- **HuggingFace** - Embeddings & transformers
- **PyTorch** - Deep learning backend
- **Python 3.13** - Programming language

---

**Author:** Zahid Iqbal  
**Last Updated:** March 3, 2026
