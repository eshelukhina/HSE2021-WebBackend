from pydantic import BaseModel


class MedicalCard(BaseModel):
    name: str
    age: int
    gender: str
    diagnosis: str
