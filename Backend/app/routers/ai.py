from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.agent import crm_agent

router = APIRouter(
    prefix="/ai",
    tags=["AI Agent"],
)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    result = crm_agent.invoke(
        {
            "message": request.message,
            "response": "",
        }
    )

    return {
        "response": result["response"],
    }