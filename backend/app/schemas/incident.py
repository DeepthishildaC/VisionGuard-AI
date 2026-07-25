from pydantic import BaseModel
from typing import Optional


class IncidentCreate(BaseModel):
    event_type: str
    risk_level: str = "LOW"
    description: Optional[str] = None
    confidence: Optional[float] = None
    image_path: Optional[str] = None
    video_path: Optional[str] = None
    camera_id: int


class IncidentUpdate(BaseModel):
    event_type: Optional[str] = None
    risk_level: Optional[str] = None
    description: Optional[str] = None
    confidence: Optional[float] = None
    image_path: Optional[str] = None
    video_path: Optional[str] = None
    status: Optional[str] = None
    is_resolved: Optional[bool] = None


class IncidentResponse(BaseModel):
    id: int
    event_type: str
    risk_level: str
    status: str
    is_resolved: bool
    confidence: Optional[float]
    camera_id: int

    class Config:
        from_attributes = True