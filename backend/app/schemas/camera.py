from pydantic import BaseModel


class CameraCreate(BaseModel):
    camera_name: str
    location: str
    stream_url: str
    ip_address: str | None = None
    camera_type: str = "IP Camera"
    resolution: str = "1920x1080"
    fps: int = 30
    ai_enabled: bool = True


class CameraUpdate(BaseModel):
    camera_name: str | None = None
    location: str | None = None
    stream_url: str | None = None
    status: str | None = None
    ai_enabled: bool | None = None


class CameraResponse(BaseModel):
    id: int
    camera_name: str
    location: str
    status: str
    ai_enabled: bool

    class Config:
        from_attributes = True