# import random
# import string
# import unittest
# from random import seed
# from random import randint
#
# from logic.card import is_valid_name, is_valid_age, is_valid_patient
# from models.medical_cards import MedicalCard
#
#
# def randomString(N):
#     return ''.join(random.choice(string.punctuation + string.ascii_letters + string.digits + ' ') for _ in range(N))
#
#
# class MyTestCase(unittest.TestCase):

#
#     def test_is_valid_patient(self):
#         for x in range(0, 1000):
#             seed(x)
#             pat = MedicalCard(name=randomString(x), age=randint(-1000, 1000), gender=randomString(x),
#                               diagnosis=randomString(x))
#             word_list = pat.name.split()
#             number_of_words = len(word_list)
#             if number_of_words == 2 and pat.age >= 0:
#                 self.assertEqual(is_valid_patient(pat), True)
#             else:
#                 self.assertEqual(is_valid_patient(pat), False)
#
#
# # if __name__ == '__main__':
# #     unittest.main()
