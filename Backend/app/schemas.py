from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InteractionCreate(BaseModel):
    hcp_name: str
    hospital: str
    specialization: str
    discussion: str
    follow_up: Optional[str] = None


class InteractionUpdate(BaseModel):
    hcp_name: str
    hospital: str
    specialization: str
    discussion: str
    follow_up: Optional[str] = None


class InteractionResponse(BaseModel):
    id: int
    hcp_name: str
    hospital: str
    specialization: str
    discussion: str
    summary: str
    follow_up: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True