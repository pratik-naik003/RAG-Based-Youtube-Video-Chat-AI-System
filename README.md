# 🎥 RAG-Based YouTube Video Chat AI (Streaming)

A **Retrieval-Augmented Generation (RAG)** based web application that allows users to **ask questions about any YouTube video** and receive **real-time streamed answers** from an LLM using the video’s transcript as context.

The system extracts the YouTube transcript, chunks it, stores it in a vector database (FAISS), retrieves relevant context, and streams answers token-by-token to the frontend.

---

## 🚀 Features

* 🔗 YouTube Transcript Extraction
* 🧠 RAG Pipeline using LangChain
* 📦 FAISS Vector Store
* 🔍 Semantic Search with HuggingFace Embeddings
* ⚡ Real-time Streaming LLM Output
* 🌐 FastAPI Backend
* 🎨 Clean & Modern HTML/CSS Frontend
* 🚫 No Chain-of-Thought / Thinking Tokens Shown

---

## 🧩 Tech Stack

### Backend

* FastAPI
* LangChain
* FAISS
* HuggingFace Embeddings (`all-MiniLM-L6-v2`)
* ChatCerebras (Qwen-3-32B)
* YouTube Transcript API
* Pydantic
* Python

### Frontend

* HTML
* CSS
* JavaScript (Fetch Streaming API)

---

## 📂 Project Structure

```
.
├── Backend/
│   ├── rag_with_chain.py      # RAG pipeline + streaming logic
│   ├── routes.py              # FastAPI routes
│   ├── schema.py              # Pydantic input schema
│   ├── transcript.py          # YouTube transcript extraction
│
├── index.html                 # Frontend UI
├── .env                       # Environment variables
├── requirements.txt
└── README.md
```

---

## 🔁 How It Works (Flow)

1. User enters:

   * YouTube video URL
   * Question
2. Backend:

   * Extracts video transcript
   * Splits transcript into chunks
   * Generates embeddings
   * Stores embeddings in FAISS
   * Retrieves top relevant chunks
3. LLM:

   * Uses **ONLY retrieved context**
   * Streams response token-by-token
4. Frontend:

   * Displays live streamed answer
   * Removes `<think>` / reasoning output

---

## 🧠 RAG Prompt Design

The system prompt enforces:

* Answer **ONLY from transcript**
* No chain-of-thought
* Structured & clear answers
* Graceful fallback if info not found

```
Use ONLY the provided transcript context.
Do NOT include your reasoning, chain-of-thought, or internal thinking.
Provide ONLY the final answer in a clear, structured format.
```

---

## 📡 API Endpoint

### POST `/chat-stream`

**Request Body**

```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "prompt": "Your question here"
}
```

**Response**

* `text/plain`
* Streamed response (chunk-by-chunk)

---

## 🖥️ Frontend Preview

* Gradient modern UI
* Live typing indicator
* Markdown-style formatting
* Auto-scroll streaming output
* Error handling for backend issues

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables (`.env`)

```env
CEREBRAS_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend Server

```bash
uvicorn Backend.routes:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 🌐 Run Frontend

Simply open:

```
index.html
```

in your browser.

---

## ⚠️ Limitations

* Only works for videos with English transcripts
* Transcript-based answers only (no hallucination)
* Requires valid Cerebras API key

---

## 🚧 Future Improvements

* Multi-language transcript support
* Persistent vector storage
* Authentication
* Mobile-friendly UI
* Multi-video RAG support

---

## 🙌 Credits

* LangChain
* Cerebras
* HuggingFace
* YouTube Transcript API
* FastAPI

---

## 📜 Project Author 
Pratik naik
Walchand College of engineering sangli

