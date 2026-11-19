from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question : str = Field(min_length=3)
    temperature : float = Field(default=0.7, ge=0, le=2)
    max_tokens : int = Field(default=500, ge=1, le=2000)
    model : str = Field(default="openai/gpt-oss-120b")

request = ChatRequest(
    question="Explain embeddings"
)

print(request.model_dump())