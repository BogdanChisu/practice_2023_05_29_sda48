"""
Scrieti o functie care sa genereze json cu cheile nume, prenume si varsta, iar valorile sa fie aleatoare
(hint- libraria random)
"""
import random
import string
import json

def genereaza_persoana_aleatorie():
    litere = string.ascii_letters
    nume = ''.join(random.choice(litere) for i in range(3, 10))
    prenume = ''.join(random.choice(litere) for i in range(3, 10))
    varsta = random.randint(1, 130)

    persoana = {
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta
    }
    return persoana

def genereaza_json_file(nr_persoane):
    for i in range(nr_persoane):
        persoana_i = genereaza_persoana_aleatorie()
        json_obj= json.dumps(persoana_i, indent=2)
        with open("sample.json", "a") as file:
            file.write(json_obj)

genereaza_json_file(4)