import builtwith    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from techdetailsapp.WebStackChecker import WebStackChecker

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def getTechStackDetails():
    # return {"cdn": "Hello World"}
    url = "https://www.typescriptlang.org/"
    d = WebStackChecker(url).techStack()
    return d
