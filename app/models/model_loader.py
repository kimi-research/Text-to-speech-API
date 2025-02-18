import warnings

import torch
import torch.nn as nn
from style_bert_vits2.nlp import bert_models
from style_bert_vits2.constants import Languages
from style_bert_vits2.tts_model import TTSModel

# ignore FutureWarning
warnings.simplefilter("ignore", FutureWarning)

class SBV2Model(nn.Module):
    def __init__(self, model_path, config_path, style_vec_path, **kwargs):
        """Initialize Style-Bert-VITS2 model"""
        super(SBV2Model, self).__init__()
        # Load BERT model
        bert_models.load_model(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
        bert_models.load_tokenizer(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
        # Load TTS model
        self.model = TTSModel(
            model_path=model_path,
            config_path=config_path,
            style_vec_path=style_vec_path,
            device="cpu",
        )

    def forward(self, text):
        """Text-to-speech synthesis"""
        sr, audio = self.model.infer(
            text=text,
            language=Languages.JP
        )

        return audio, sr

def load_model(model_type, **kwargs):
    # available TTS class
    model_classes = {"SBV2": SBV2Model}
    # Define TTS model
    model = model_classes[model_type](**kwargs)
    model.eval()
    return model
