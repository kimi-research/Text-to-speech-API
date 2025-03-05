import random

from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from urllib.parse import urlparse

from app.services.inference import predict
from app.schemas import TextInput 


router = APIRouter()
# Set template
templates = Jinja2Templates(directory="app/templates")
# Set max text length to avoid OOM
MAX_TEXT_LENGTH = 20

# Page to display the form
@router.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    # nginx から送信された `X-Forwarded-Prefix` を取得 (リバースプロキシとの不整合を解消)
    forwarded_prefix = request.headers.get("X-Forwarded-Prefix", "")

    # `/tts/` の場合は `/tts/generate/` に、それ以外は `/generate/` に設定
    form_action = f"{forwarded_prefix}/generate/"
    return templates.TemplateResponse("index.tmp.html", {"request": request, "form_action": form_action})

@router.post("/generate/")
async def get_prediction(input_data: TextInput):
    text = input_data.text.strip()
    print(f"Requested text: {text}")
    # check the length of input text
    if len(text) > MAX_TEXT_LENGTH:
        return JSONResponse(
            status_code=400,
            content={"message": f"入力テキストが長すぎます。 {MAX_TEXT_LENGTH}文字以内で再度お試しください。"}
        ) 
    # TTS
    saved_audio_path = predict(text)
    return FileResponse(
        saved_audio_path,
        media_type="audio/mpeg",
        filename=f"{random.randint(10**9, 10**10 - 1)}.mp3"
    )

