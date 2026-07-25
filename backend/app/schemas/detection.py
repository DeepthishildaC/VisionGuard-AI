from pydantic import BaseModel
from typing import Optional


class DetectionCreate(BaseModel):
    object_type: str
    confidence: float
    track_id: Optional[int] = None
    bounding_box: Optional[str] = None
    incident_id: int


class DetectionUpdate(BaseModel):
    object_type: Optional[str] = None
    confidence: Optional[float] = None
    track_id: Optional[int] = None
    bounding_box: Optional[str] = None


class DetectionResponse(BaseModel):
    id: int
    object_type: str
    confidence: float
    track_id: Optional[int]
    bounding_box: Optional[str]
    incident_id: int

    class Config:
        from_attributes = True