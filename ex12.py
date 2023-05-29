"""
creati o functie care returneaza un dictionar, folosing dict comprehension, in care cheile sunt numere intre a si b,
iar valorile sunt tuples cu (patratul numarului, radacina patrata rotunjita la 2 decimale).
Ex functia dict_func(2,4) returneaza {2:(4, 1,41), 3:(9, 1.73), 4: (16, 2)}
"""
from math import sqrt

def dict_func(a, b):
    return {x: (x * x, round(sqrt(x), 2)) for x in range(a, b +1)}

print(dict_func(2, 4))