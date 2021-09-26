from models.medical_cards import MedicalCard
from datetime import datetime, date


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
    return date <= date.today()


def is_valid_patient(card: MedicalCard):
    if is_valid_name(card.name) and is_valid_age(card.age) and is_valid_date(card.DOB):
        return True
    return False



