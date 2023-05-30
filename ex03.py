"""
Creați un generator care returnează numere pare de la 0 la n, care se divid cu 7, folosind cuvântul cheie yield
"""

def seven_div_gen(n):
    for i in range(0, n+1, 14):
        #if i % 14 == 0:
        yield i

n = int(input("Introduceti numarul n: "))
list_seven_div = list(seven_div_gen(n))
print(list_seven_div)
