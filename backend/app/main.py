from fastapi import FastAPI

from app.database.database import engine
from app.models.base import Base

# Import all models so SQLAlchemy knows about them
from app.models import *

# Import routers
from app.api.v1.auth import router as auth_router

from app.api.v1.cameras import router as camera_router

from app.api.v1.incidents import router as incident_router

from app.api.v1.detections import router as detection_router

from app.api.v1.alerts import router as alert_router

from app.api.v1.ai_summaries import router as ai_summary_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VisionGuard AI",
    version="1.0.0",
    description="AI-Powered CCTV Incident Detection and Security Copilot",
)

# Register routers
app.include_router(auth_router)
app.include_router(camera_router)
app.include_router(incident_router)
app.include_router(detection_router)
app.include_router(alert_router)
app.include_router(ai_summary_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to VisionGuard AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }