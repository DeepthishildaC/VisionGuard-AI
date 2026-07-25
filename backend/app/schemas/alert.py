from pydantic import BaseModel
from typing import Optional


class AlertCreate(BaseModel):
    title: str
    message: str
    severity: str = "MEDIUM"
    status: str = "ACTIVE"
    is_read: bool = False
    incident_id: int


class AlertUpdate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    is_read: Optional[bool] = None


class AlertResponse(BaseModel):
    id: int
    title: str
    message: str
    severity: str
    status: str
    is_read: bool
    incident_id: int

    class Config:
        from_attributes = True