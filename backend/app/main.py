from fastapi import FastAPI

app = FastAPI(
    title="VisionGuard AI",
    version="1.0.0",
    description="AI-Powered CCTV Incident Detection and Security Copilot"
)


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