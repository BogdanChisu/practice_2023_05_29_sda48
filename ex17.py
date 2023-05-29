"""
Folosind list comprehension creati o functie ce returneaza o lista care contine (x_patrat + 2) impartit la (x_cub + 3)
(rotunjit la 2 decimale) pentru x intre a si b
"""
def list_custom(a, b):
    return [round((x * x + 2) / (x ** 3 + 3), 2) for x in range(a, b + 1)]

print(list_custom(2, 7))
# [0.55, 0.37, 0.27, 0.21, 0.17, 0.15]