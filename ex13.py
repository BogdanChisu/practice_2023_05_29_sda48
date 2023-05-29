"""
Creati o lista cu patratele numerelor de la a la b daca a doua cifra in numar este 2,3 sau 4. Folositi list
comprehesion doar
"""

def return_list_squares_with_234(a, b):
    return [x * x for x in range(a, b + 1) if str(x)[1] == "2" or str(x)[1] == "3" or str(x)[1] == "4"]

print(return_list_squares_with_234(100, 150))