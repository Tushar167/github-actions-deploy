from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "i am trying out a ci cd pipeline"}

@app.get("/trialApi")
def trial_api():
    return {"message": "This is a trial API endpoint"}

@app.get("/someApi")
def some_api():
    return {"info": "This is some API endpoint"}

@app.get("/hereApi")
def here_api():
    return {"detail": "This is here API endpoint"}