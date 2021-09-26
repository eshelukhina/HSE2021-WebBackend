import random
import string
from datetime import date
from random import randint
from random import seed

from application.logic.card import is_valid_name, is_valid_age, is_valid_date


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
