"""
Creati o functie care primeste un argument tuple cu mai multe cuvinte si un substring, si returneaza un tuple doar cu
cuvintele ce nu contin substring dat ca argument functiei.
 de exemplu functia fx(('măr', 'pere', 'banane', 'ananas', 'struguri'), "a") returneaza ('măr', 'pere', 'struguri')
"""

def fx(a_tuple, a_str):
    return tuple(x for x in (a_tuple) if a_str not in x)

print(fx(('măr', 'pere', 'banane', 'ananas', 'struguri'), "a"))