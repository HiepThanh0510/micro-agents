"""
Main FastAPI application for the LLM Hub API.
"""


from configs import settings
from fastapi import FastAPI
from models import CompletionRequest, CompletionResponse
from ollama import AsyncClient

app = FastAPI(
    title="LLM Hub API",
    description="API for interacting with various LLM providers",
    version="0.1.0",
)


@app.get("/")
async def models():
    """
    Get a list of available models.

    Returns:
        JSON response containing the list of models
    """
    client = AsyncClient(host=settings.OLLAMA_BASE_URL)
    models_list = await client.list()
    return {"models": models_list.models}


@app.post("/completions")
async def completions(request: CompletionRequest) -> CompletionResponse:
    """
    Generate a completion for a given prompt.
    """
    model = request.model
    prompt = request.prompt

    client = AsyncClient(host=settings.OLLAMA_BASE_URL)
    response = await client.chat(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return CompletionResponse(content=response.message.content, model=response.model)
