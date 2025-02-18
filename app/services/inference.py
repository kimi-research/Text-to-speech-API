import os

import soundfile as sf
import torch

from models.model_loader import load_model

model_root = "app/models/weights/Style-Bert-VITS2"
model_path = "jvnv-F1-jp/jvnv-F1-jp_e160_s14000.safetensors"
config_path = "jvnv-F1-jp/config.json"
style_vec_path = "jvnv-F1-jp/style_vectors.npy"

model = load_model(
    model_type="SBV2",
    model_path=os.path.join(model_root, model_path),
    config_path=os.path.join(model_root, config_path),
    style_vec_path=os.path.join(model_root, style_vec_path),
    device="cpu"
)

def predict(text: str, outpath: str = "output/output.mp3"):
    # Inference (for TTS)
    with torch.no_grad():
        audio, sr = model(text)
    # Save audio
    if not os.path.exists(os.path.dirname(outpath)):
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
    sf.write(outpath, audio, sr)
    return outpath
