from fastapi import FastAPI
from 

app=FastAPI()


@app.get("/")
def home():
  return {"hello " : "server is running"}