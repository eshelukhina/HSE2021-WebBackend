from models.medical_cards import MedicalCard
from datetime import datetime, date

patient1 = MedicalCard(name="Dan Reynolds",
                       age=34,
                       gender="Male",
                       diagnosis="Ankylosing spondylitis",
                       DOB=date(day=14, month=7, year=1987)
                       )
patient2 = MedicalCard(name="Morgan Freeman",
                       age=84,
                       gender="Male",
                       diagnosis="Fibromyalgia",
                       DOB=date(day=1, month=6, year=1937)
                       )
data = {
    1: patient1,
    2: patient2
}
