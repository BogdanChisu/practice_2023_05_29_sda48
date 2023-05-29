"""
Avand o lista cu 5 nume si 5 varste, creati un dictionar cu list comprehension care sa aiba numele chei si varsta ca
valoare.
Hint: daca aveti o lista cu nume, varsta, vedeti ce face zip(nume, varsta) si astfel putei itera key, value in
zip(nume, varsta)
"""

def return_name_age_dict(the_list):
    name_list = the_list[:5]
    age_list = the_list[5:]
    the_dict = dict(zip(name_list, age_list))
    return the_dict

item_list = ['Bobonete', 'Rapidoaica', 'Firicel', 'Aspirina', 'Gianina', 30, 45, 32, 34, 23]

print(return_name_age_dict(item_list))