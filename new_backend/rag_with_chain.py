from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cerebras import ChatCerebras
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def rag_answer_stream(text_transcript: str, user_prompt: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.create_documents([text_transcript])
    
    embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-v2"
)

    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 20}
    )

    llm = ChatCerebras(
        model="qwen-3-32b",
        streaming=True   # ✅ IMPORTANT
    )

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.

Use ONLY the provided transcript context.
Do NOT include your reasoning, chain-of-thought, or internal thinking.
Provide ONLY the final answer in a clear, structured format (bullet points or steps).

If the context is insufficient, respond with:
"I was not found much information about your question thank you."



        {context}
        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        RunnableParallel({
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        })
        | prompt
        | llm
        | StrOutputParser()
    )

    #
    for chunk in chain.stream(user_prompt):
        yield chunk
