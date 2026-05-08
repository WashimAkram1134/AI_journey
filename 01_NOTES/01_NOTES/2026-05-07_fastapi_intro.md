API = Application Programming Interface
Simple meaning:
A way for software systems to communicate.

🔥 REAL LIFE ANALOGY
Suppose:
You = customer
Kitchen = backend logic
Waiter = API
You don’t enter kitchen directly.
You tell waiter:
“Give biryani.”
Waiter takes request → kitchen processes → waiter returns response.


📘 THEORY — WHAT IS UVICORN?
Your Python code alone cannot serve web requests.
Need a server.
Uvicorn runs your FastAPI app.
Think:
FastAPI = brain
Uvicorn = delivery vehicle



@app.get("/")
This is VERY IMPORTANT.
This is called:
Decorator
Decorators are advanced Python features heavily used in FastAPI.
means:
“When browser/client sends GET request to homepage, execute next function.”

("/")
This is route path.
/ means:
homepage/root URL
Example:
http://127.0.0.1:8000/
The / part is route.

Method
Meaning
GET
read data
POST
send/create data
PUT
update
DELETE
delete




Remember earlier:
Python dict
JSON
FastAPI internally converts:
Python dict → JSON response
This is why understanding JSON earlier was critical.
🔥 COMPLETE REQUEST FLOW
Let’s visualize FULL system.

STEP 1
Browser requests:
http://127.0.0.1:8000/

STEP 2
Uvicorn server receives request.

STEP 3
FastAPI checks routes.
Finds:
@app.get("/")







Suppose my code have a about function. 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI Engineer Journey API"}

@app.get("/about")# suppose about na likhe likhlam app.get(/info). Tahole about function run krte “http://127.0.0.1:8000/info”

def about():
    return {
        "name": "Washim",
        "goal": "Become AI Engineer",
        "focus": "Generative AI"
    }


To run this function 

http://127.0.0.1:8000/about

STEP 4
Runs:
home()

STEP 5
Function returns dictionary.

STEP 6
FastAPI converts dict → JSON.

STEP 7
Browser receives JSON response.

