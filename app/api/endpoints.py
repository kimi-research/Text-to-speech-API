from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.services.inference import predict


router = APIRouter()
# Set template
templates = Jinja2Templates(directory="app/templates")

# Page to display the form
@router.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate/")
async def get_prediction(text: str = Form(...)):
    # TTS
    saved_audio_path = predict(text)
    return FileResponse(saved_audio_path, media_type="audio/mpeg", filename="gen_speech.mp3")
