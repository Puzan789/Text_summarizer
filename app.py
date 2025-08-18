from fastapi import FastAPI  # Correct import of the FastAPI class

import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI() 


@app.get("/",tags=["authentication"])
async def rindex():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response ("Training Successfull")
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/predict")
async def predict(text: str):
    try:
        pipeline=PredictionPipeline()
        summary=pipeline.predict(text)
        return summary
    except Exception as e:
        raise e