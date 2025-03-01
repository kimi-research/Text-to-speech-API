#!/bin/bash
# activate virtual env
source /home/k_hattori/Text-to-speech-API/venv/bin/activate
# set LOGFILE
LOGFILE="startat_$(date '+%Y%m%d_%H%M%S').log"
# Start API (fastAPI)
nohup uvicorn app.main:app --host=0.0.0.0 --port=80 &> "$LOGFILE" &
