from fastapi import FastAPI

app = FastAPI(
    title="AI Enterprise Knowledge Assistant",
    description="Backend API for the AI Enterprise Knowledge Assistant",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Enterprise Knowledge Assistant API is running",
        "status": "success"
    }