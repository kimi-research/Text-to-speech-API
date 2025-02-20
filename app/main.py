from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Text-to-speech synthesis API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
