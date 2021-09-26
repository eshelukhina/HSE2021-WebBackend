import random
import string
from datetime import date
from random import randint
from random import seed

from application.db.fake_db import data
from application.logic.card import is_valid_name, is_valid_age, is_valid_date, delete_appointment, delete_visit
from application.models.medical_cards import Appointment, Doctor, Hospital, MedicalCard, Visit


def randomString(N):
    return ''.join(random.choice(string.punctuation + string.ascii_letters + string.digits + ' ') for _ in range(N))


def test_is_valid_name():
    for x in range(0, 1000):
        rnd_str = randomString(x)
        word_list = rnd_str.split()
        number_of_words = len(word_list)
        if number_of_words == 2:
            assert is_valid_name(rnd_str) == True
        else:
            assert is_valid_name(rnd_str) == False


def test_is_valid_age():
    for x in range(0, 1000):
        seed(x)
        num = randint(-1000, 1000)
        if num >= 0:
            assert is_valid_age(num) == True
        else:
            assert is_valid_age(num) == False


def test_is_valid_date():
    assert is_valid_date(date.today()) == False
    assert is_valid_date(date(day=7, month=12, year=2018)) == True


def test_delete_appointment():
    patient_id = 1
    data.clear()
    app1 = Appointment(doctor=Doctor(name="Doc1"), hospital=Hospital(id=1), time=date(year=2020, month=7, day=13))
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
    visit = Visit(doctor=Doctor(name="Doc1"), time=date(year=2020, month=7, day=13), hospital=Hospital(id=1),
                  info="fjeifj")
    delete_appointment(visit, 1)
    assert len(patient1.info.appointment) == 1


def test_delete_visit():
    patient_id = 1
    data.clear()
    patient1 = MedicalCard(name="Dan Reynolds",
                           age=34,
                           gender="Male",
                           diagnosis="Ankylosing spondylitis",
                           DOB=date(day=14, month=7, year=1987)
                           )
    visit1 = Visit(doctor=Doctor(name='Doc1'), time=date(year=2020, month=7, day=13), hospital=Hospital(id=1),
                   info="fjeifj")
    visit2 = Visit(doctor=Doctor(name='Doc1'), time=date(year=2020, month=7, day=13), hospital=Hospital(id=1),
                   info="")
    data[patient_id] = patient1
    patient1.info.visit.append(visit1)
    patient1.info.visit.append(visit2)
    delete_visit(visit1, 1)
    assert len(patient1.info.visit) == 1
