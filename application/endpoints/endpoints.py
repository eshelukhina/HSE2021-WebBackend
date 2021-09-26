from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from application.db.fake_db import data
from application.logic.card import is_valid_patient, add_visit_helper
from application.logic.card import check_other_appointments
from application.logic.card import delete_appointment
from application.logic.card import delete_visit
from application.models.medical_cards import MedicalCard
from application.models.medical_cards import Appointment
from application.models.medical_cards import Visit

router = APIRouter(prefix="/Patients", tags=["Patients"])


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


@router.post("/add_appointment")
async def add_appointment(patient_id: int, new_appointment: Appointment):
    if patient_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    else:
        card = data[patient_id]
        check_other_appointments(patient_id)
        card.info.appointment.append(new_appointment)
    return data[patient_id]


@router.post("/add_visit")
async def add_visit(patient_id: int, new_visit: Visit):
    if patient_id not in data:
        raise HTTPException(status_code=400, detail="Id does not exist")
    else:
        card = data[patient_id]
        if new_visit in card.info.visit:
            raise HTTPException(status_code=400, detail="Visit already exists")
        else:
            add_visit_helper(patient_id, new_visit)
    return data[patient_id]
