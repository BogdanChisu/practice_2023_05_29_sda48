"""
Creati o functie care calculeaza suma patratelor argumentelor date functiei, un numar nedeterminat de argumente
(hint: *args).
Folositi try-except pentru a verifica daca argumentele date functiei sunt valide.
"""

def sum_of_squares(*args):
    sum_squares = 0
    for arg in args:
        try:
            sum_squares += arg * arg
        except TypeError:
            print(f"Expected type int or float, received {type(arg)} ")
    return sum_squares

try:
    # print(sum_of_squares(1, g, 2, 'e', 4))  # => Undeclared variable name 'g' is not defined
    print(sum_of_squares(1, 2, 'e', 4))  # => Expected type int or float, received <class 'str'> \n 21
except NameError as er:
    print(f"Undeclared variable {er}")