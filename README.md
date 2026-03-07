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

### 4. Prompts & Prompt Templates
- **Location:** `langchain_prompt/`
- `PromptTemplate` — dynamic variable-based prompts
- `ChatPromptTemplate` with `SystemMessagePromptTemplate` & `HumanMessagePromptTemplate`
- `MessagesPlaceholder` — chat history injection into prompts
- `SystemMessage`, `HumanMessage`, `AIMessage` — direct message-type usage
- Streamlit UI integration for interactive research paper summarizer (`prompt2.py`, `prompt_ui.py`)
- Multi-parameter prompts: paper selection, explanation style & length

### 5. Structured Output
- **Location:** `StructuredOutput/`
- `pydantic.py` — Pydantic `BaseModel` for defining strongly-typed structured schemas
- `type_dict.py` — Python `TypedDict` for lightweight typed dictionary structures
- `structuretypedict.py` — LangChain `with_structured_output()` using `TypedDict` with Google Gemini (`gemini-2.5-flash`) — movie review summary & sentiment extraction
- `json_schema.json` — Raw JSON Schema definition for structured data validation

### 6. Chains
- **Location:** `chains/`
- `simplechain.py` — Basic `prompt | model | parser` chain with ASCII graph visualization
- `complexchain.py` — Multi-step sequential chain: report generation → auto-summarization
- `parralelchain.py` — `RunnableParallel` running two LLM calls concurrently (notes + questions) then merging with a third chain
- `conditionalchain.py` — `RunnableBranch` for sentiment-based conditional routing using `PydanticOutputParser`

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
│   └── llm_demo.py
├── 2.ChatModels/
│   ├── chatmodel1.py
│   ├── chatmodel2.py
│   ├── chatmodel3.py
│   ├── chatmodel4.py
│   └── chatmodel5.py
├── 3.Embeddings/
│   ├── embedding1.py
│   └── embedding2.py
├── langchain_prompt/
│   ├── message.py
│   ├── chatplaceholder.py
│   ├── prompt_ui.py
│   └── prompt2.py
├── StructuredOutput/
│   ├── pydantic.py
│   ├── type_dict.py
│   ├── structuretypedict.py
│   └── json_schema.json
├── chains/
│   ├── simplechain.py
│   ├── complexchain.py
│   ├── parralelchain.py
│   └── conditionalchain.py
├── requirements.txt
├── .env
└── README.md
```

## Next Steps 🚀
Aage aur LangChain components add kiye jayenge:
- ~~Prompts & Prompt Templates~~ ✅
- ~~Structured Output~~ ✅
- ~~Chains~~ ✅
- Memory
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
**Last Updated:** March 7, 2026
