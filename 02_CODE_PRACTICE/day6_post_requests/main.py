from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# REQUEST BODY MODEL
class TextInput(BaseModel):
    text: str


# HOME ROUTE
@app.get("/")
def home():

    return {
        "message": "Welcome to Day 6 POST API"
    }


# SUMMARIZE API
@app.post("/summarize")
def summarize(data: TextInput):

    short_text = data.text[:5]

    return {
        "original_text": data.text,
        "summary": short_text
    }


# UPPERCASE API
@app.post("/uppercase")
def uppercase(data: TextInput):

    upper_text = data.text.upper()

    return {
        "original_text": data.text,
        "uppercase_text": upper_text
    }


# WORD COUNT API
@app.post("/wordcount")
def word_count(data: TextInput):

    words = data.text.split()

    total_words = len(words)

    return {
        "text": data.text,
        "total_words": total_words
    }