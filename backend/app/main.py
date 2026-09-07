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

from app.routes.camera_stream import router as camera_stream_router

from app.routes.websocket import router as websocket_router

from fastapi import WebSocket, WebSocketDisconnect

from app.websocket.manager import manager

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
app.include_router(camera_stream_router)
app.include_router(websocket_router)



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

@app.websocket("/ws/incidents")
async def websocket_incidents(websocket: WebSocket):
    """
    Real-time incident WebSocket.
    """

    await manager.connect(websocket)

    try:
        while True:
            # Keep the connection alive
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)