from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"Welcome to Day-5 of AI journey"}


@app.get("/summarize")
def summarize(text:str):
    short_text=text[:50]
    return{
    "Original text":text,
    "Summury of this text":short_text

}

@app.get("/wordcount")
def word_count(text:str):
    word=text.split()
    total_word=len(word)
    return{
        "text":text,
        "Total word count":total_word
    }

#character count

@app.get("/charcount")
def char_count(text: str):

    total_characters = len(text)

    return {
        "text": text,
        "total_characters": total_characters
    }