from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from db.fake_db import data
from logic.card import MedicalCard, is_valid_patient

router = APIRouter(prefix="/Patients", tags=["Patients"], )


@router.get("/id")
async def get_by_id(patient_id: Optional[int] = None):
    if patient_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    return data[patient_id]


@router.post("/add_patient")
async def add_patient(patient_id: int, card: MedicalCard):
    if patient_id in data:
        raise HTTPException(status_code=400, detail="Patient already exist")
    if is_valid_patient(card):
        data[patient_id] = card
        return data[patient_id]
    else:
        raise HTTPException(status_code=400, detail="Invalid patient params. Name must contains firstname and "
                                                    "lastname. Age must be >= 0")
