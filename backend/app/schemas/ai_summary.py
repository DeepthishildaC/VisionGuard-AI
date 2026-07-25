from pydantic import BaseModel
from typing import Optional


class AISummaryCreate(BaseModel):
    summary: str
    model_name: str
    confidence: Optional[str] = None
    incident_id: int


class AISummaryUpdate(BaseModel):
    summary: Optional[str] = None
    model_name: Optional[str] = None
    confidence: Optional[str] = None


class AISummaryResponse(BaseModel):
    id: int
    summary: str
    model_name: str
    confidence: Optional[str]
    incident_id: int

    class Config:
        from_attributes = True