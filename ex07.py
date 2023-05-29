"""
Scrieti o functie lambda care calculeaza x_la_puterea_y - radacina_patrata(x)
"""
from math import sqrt
resultx = lambda x, y: x ** y - sqrt(x)
print(resultx(4, 2)) # 4^2 - sqrt(4) = 16 - 2 = 14  