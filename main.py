
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

ANSWER = {
    "A": {
        "steps": ["L3", "L4", "L5"],
        "seconds": 43
    },
    "B": {
        "steps": ["L1", "L2", "L3", "L4", "L5"],
        "seconds": 113
    },
    "C": {
        "steps": [],
        "seconds": 0
    },
    "D": {
        "steps": [],
        "seconds": 0
    },
    "E": {
        "steps": ["L4", "L5"],
        "seconds": 43
    }
}


@app.get("/")
def get_answer():
    return JSONResponse(content=ANSWER)
