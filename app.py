from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import os

load_dotenv()
key = os.getenv("key")

app = FastAPI()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=key
)

storage = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=storage
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Welcome to Gemini Chatbot"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    response = conversation.run(user_message)
    return {"user": user_message, "response": response}
