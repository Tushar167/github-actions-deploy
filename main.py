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

@app.gert("/someApi")
def some_api():
    return {"info": "This is some API endpoint"}