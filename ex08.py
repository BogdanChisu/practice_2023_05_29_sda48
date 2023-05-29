"""
Extrageți dintr-un text toate fragmentele care respectă formatul de număr de telefon românesc: +40xxxxxxxxx, cu regex.
Nu vă complicați cu detalii, faceți ceva good enough, că detalii ar fi destule ce v-ar încetini.
"""
import re

def get_phone_numbers(a_text):
    phone_no_candidates = re.split(" ", a_text) # splits the string input into a list of strings
    print(phone_no_candidates)
    for phone_no_candidate in phone_no_candidates:
        regex_b = r'\A[+].{10}\d' # starts with "+" followed by 10 digits
        phone_nos = re.findall(regex_b, phone_no_candidate)
        if len(phone_nos) == 1:
            print(phone_no_candidate)

my_text = input("Insert a text: ")
get_phone_numbers(my_text) # +40741752279 QWEQWE 46456 1SDFS3 => +40741752279