from pydantic import BaseModel


class CompletionRequest(BaseModel):
    model: str
    prompt: str


class CompletionResponse(BaseModel):
    model: str
    content: str
