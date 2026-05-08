from fastapi import FastAPI # pyright: ignore[reportMissingImports]
app = FastAPI()
@app.get("/")  # This is route path.
def home():
    return {"Welcome to your AI journey FastAPI.\n I am Washim Akram For your service sir"}

@app.get("/info") #http://127.0.0.1:8000/about
def about():
    return{"Name":"Washim Akram",
 "Age":25,
 "ID":1134}


#DYNAMIC URL PARAMETER

@app.get("/welcome/{name}")
def greet(name:str):
    return f"Hello Mr/Mrs {name}, to our AI Journey" #"Hello Mr/Mrs Washim AKram, to our AI Journey"




#🔥 UNDERSTAND WHAT JUST HAPPENED

#Browser sent request.

#FastAPI captured parameter.

#Python processed.

#JSON returned.

#This is backend engineering.*/



#summurize🔥

@app.get("/summarize") # explain in "AI AGent Journey(Notes)" doc file
def summarize(text: str):
    short_text = text[:50]

    return {
        "original_text": text,
        "summary": short_text
    }
#http://127.0.0.1:8000/summarize?text=Artificial intelligence is transforming software engineering

