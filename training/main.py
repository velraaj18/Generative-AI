# Generative AI training

# Calling an LLM using the OpenAI() API function

import os
from openai import OpenAI
from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI
from .schemas.chat import ChatRequest, ChatResponse
from pydantic import BaseModel
import asyncio
import requests

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="GenAI Engineering Lab",
    description="Learning GenAI backend development",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status : str
    application : str

@app.get("/health_check", response_model = HealthResponse)
async def Health_Check():
    return HealthResponse(
        status = "Healthy",
        application= "GenAI Engineering Lab"
    )

@app.get("/")
async def Home():
    return "Welcome to Generative AI Lab"

@app.post("/chat", response_model= ChatResponse)
async def Chat(request: ChatRequest):
    return ChatResponse(
        question= f"You asked question, {request.question}",
        answer = request.question,
        model = request.model
    )



