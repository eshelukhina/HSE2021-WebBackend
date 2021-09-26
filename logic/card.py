from models.medical_cards import MedicalCard
from datetime import datetime, date
from db.fake_db import data
from models.medical_cards import Visit


def is_valid_name(name):
    word_list = name.split()
    number_of_words = len(word_list)
    if number_of_words == 2:
        return True
    return False


def is_valid_age(age):
    if age >= 0:
        return True
    return False


def is_valid_date(date: date):
    return date <= date(day=1, month=1, year=2020)


def is_valid_patient(card: MedicalCard):
    if is_valid_name(card.name) and is_valid_age(card.age) and is_valid_date(card.DOB):
        return True
    return False


def check_other_appointments(patient_id: int):
    patient = data[patient_id]
    for app in patient.info.appointment:
        if app.time <= date(day=1, month=1, year=2020):
            visit = Visit(doctor=app.doctor, time=app.time, hospital=app.hospital)
            if visit not in patient.info.visit:
                patient.info.visit.append(visit)
                patient.info.appointment.remove(app)


def delete_appointment(visit: Visit, patient_id: int):
    patient = data[patient_id]
    for app in patient.info.appointment:
        if app.time == visit.time and app.doctor == visit.doctor and app.hospital == visit.hospital:
            patient.info.appointment.remove(app)


def delete_visit(visit: Visit, patient_id: int):
    patient = data[patient_id]
    for vis in patient.info.visit:
        if vis.time == visit.time and vis.doctor == visit.doctor and vis.hospital == visit.hospital and vis.info != visit.info:
            patient.info.visit.remove(vis)
