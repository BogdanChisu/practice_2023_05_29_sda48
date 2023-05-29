"""
Creați un dicționar care să conțină numărul de apariții ale fiecărui caracter dintr-un text folosind doar dictionary
comprehension.
Hint: text.count(caracter) . Caracter inseamna a,b,3,. etc.
Hint2: incercati functia set(text) pentru un oarecare text si vedeti ce obtineti.
"""

my_text = input("Introduceti un text: ")
my_dict = {x: my_text.count(x) for x in set(my_text) }
print(my_dict)