# TTS Web API

**Text-to-speech-API** is a Python-based **Text-to-Speech (TTS) inference API**.

Currently, this API supports only **[Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2.git)**.

## Setup

### 1. Install and build environment
```
$ git clone https://github.com/kimi-research/Text-to-speech-API.git
$ cd Text-to-speech-API
# Install PyTorch(cpu) at first
$ pip install -r requirements_pytorch.txt
$ pip install -r requirements.txt
```
### 2. Preparation of Style-Bert-VITS2 model
```
$ mkdir -p ./app/models/weights/Style-Bert-VITS2
$ cp -r </path/to/your/models> ./app/models/weights/Style-Bert-VITS2/<your_models>
```
### 3. Set up the model to use
```
$ vi ./app/services/inference.py
  ...
  model_path = "<your_models>/*.safetensors"
  config_path = "<your_models>/config.json"
  style_vec_path = "<your_models>/style_vectors.npy"
```
## Usage
### Launch WebAPI
```
$ ./run.sh
```
