"""
Scrieti o functie care inlocuieste toate cifrele dintr-o propozitie cu cifra-string (adica inlocuieste 2 cu doi etc)
"""

import re

digit_dictionary = {
    1: "unu",
    2: "doi",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "sase",
    7: "sapte",
    8: "opt",
    9: "noua",
    0: "zero"
}

def replace_digits(a_sentence):
    regex = r"\d"
    digits = re.findall(regex, a_sentence)
    for digit in digits:
        # print(type(digit))
        a_sentence = re.sub(regex, digit_dictionary[int(digit)], a_sentence, 1)
    print(a_sentence)


my_sentence = input("Please insert a sentence: ")
replace_digits(my_sentence)

"""
1, 2, si 3 de 0
unu, doi, si trei de zero
"""