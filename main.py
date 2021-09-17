from fastapi import FastAPI
import uvicorn
from fastapi import HTTPException

from typing import Optional

from card import MedicalCard, is_valid_patient

app = FastAPI()

data = {}


def add_card(patient_id: int, card: MedicalCard):
    data[patient_id] = card


@app.get("/id")
async def get_by_id(patient_id: Optional[int] = None):
    if patient_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    return data[patient_id]


@app.post("/add_patient")
async def add_patient(patient_id: int, card: MedicalCard):
    if patient_id in data:
        raise HTTPException(status_code=400, detail="Patient already exist")
    if is_valid_patient(card):
        data[patient_id] = card
        return data[patient_id]
    else:
        raise HTTPException(status_code=400, detail="Invalid patient params. Name must contains firstname and "
                                                    "lastname. Age must be >= 0")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, log_level="info")
