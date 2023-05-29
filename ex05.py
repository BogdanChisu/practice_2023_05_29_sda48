"""
Scrieti o functie care afiseaza toate cuvintele ce incep cu o literă minusculă sau majusculă (de ex toate cuvintele ce
încep cu A sau a), folosiți regex.
"""

import re
regex = r"^[A-Za-z]"

my_text = input("Introduceti textul de verificat: ")

words = re.split(" ", my_text)
for word in words:
    if re.findall(regex, word):
        print(word)