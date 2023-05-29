"""
Scrieti un generator care genereaza patratele perfecte intre a si b care au cifra 3 (ex- 36, 1369 etc) sau
7 (ex 576) in numar.
"""

from math import sqrt
import re

def perfect_square_w_three_and_seven(low_num, high_num):
    for i in range(low_num, high_num + 1):
        if sqrt(i) == int(sqrt(i)):
            regex = r"[37]"
            num_str = str(i)
            occurencies = re.findall(regex, num_str)
            if len(occurencies) > 0:
                yield i

a = int(input("Introduceti numarul a: "))
b = int(input("Introduceti numarul b: "))

list_rez = list(perfect_square_w_three_and_seven(a, b))
print(list_rez)

# a = sqrt(9)

# print(int(a) == a)
# print(isinstance(4.0, int))