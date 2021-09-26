import random
import string
from datetime import date
from random import randint
from random import seed

from application.db.fake_db import data
from application.logic.card import is_valid_patient, check_other_appointments
from application.models.medical_cards import MedicalCard, Appointment, Doctor, Hospital


def randomString(N):
    return ''.join(random.choice(string.punctuation + string.ascii_letters + string.digits + ' ') for _ in range(N))


def test_is_valid_patient():
    for x in range(0, 1000):
        seed(x)
        pat = MedicalCard(name=randomString(x), age=randint(-1000, 1000), gender=randomString(x),
                          diagnosis=randomString(x), DOB=date(day=7, month=12, year=2018))
        word_list = pat.name.split()
        number_of_words = len(word_list)
        if number_of_words == 2 and pat.age >= 0 and pat.DOB <= date(day=1, month=1, year=2020):
            assert is_valid_patient(pat) == True
        else:
            assert is_valid_patient(pat) == False


def test_check_other_appointments():
    patient_id = 1
    data.clear()
    app1 = Appointment(doctor=Doctor(name="Doc1"), hospital=Hospital(id=1), time=date(year=2019, month=7, day=13))
    app2 = Appointment(doctor=Doctor(name="Doc2"), hospital=Hospital(id=1), time=date(year=2021, month=7, day=13))
    patient1 = MedicalCard(name="Dan Reynolds",
                           age=34,
                           gender="Male",
                           diagnosis="Ankylosing spondylitis",
                           DOB=date(day=14, month=7, year=1987)
                           )
    patient1.info.appointment.append(app1)
    patient1.info.appointment.append(app2)
    data[patient_id] = patient1
    check_other_appointments(patient_id)
    assert len(patient1.info.appointment) == 1
    assert len(patient1.info.visit) == 1


