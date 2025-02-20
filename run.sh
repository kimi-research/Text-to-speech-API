#!/bin/bash

# Start API (fastAPI)
uvicorn app.main:app --reload
