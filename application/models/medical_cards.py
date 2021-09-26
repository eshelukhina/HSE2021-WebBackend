from datetime import date
from typing import List

from pydantic import BaseModel


class Doctor(BaseModel):
    name: str = ""


class Hospital(BaseModel):
    id: int = 0


class Visit(BaseModel):
    doctor: Doctor
    time: date = date.today()
    hospital: Hospital
    info: str = ""


class Diagnosis(BaseModel):
    doctor: Doctor
    hospital: Hospital
    now: bool = False


class Appointment(BaseModel):
    doctor: Doctor
    hospital: Hospital
    time: date = date.today()


class InfoData(BaseModel):
    visit: List[Visit]
    diagnosis: List[Diagnosis]
    appointment: List[Appointment]


class MedicalCard(BaseModel):
    name: str
    age: int
    gender: str
    diagnosis: str
    DOB: date
    info: InfoData = InfoData(visit=[], appointment=[], diagnosis=[])
