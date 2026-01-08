from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from Backend.schema import input
from Backend.transcript import get_youtube_transcript
from Backend.rag_with_chain import rag_answer_stream

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat-stream")
def chat_stream(data: input):
    transcript = get_youtube_transcript(data.url)

    return StreamingResponse(
        rag_answer_stream(transcript, data.prompt),
        media_type="text/plain"
    )
