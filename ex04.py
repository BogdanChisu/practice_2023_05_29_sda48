"""
Gestionați o excepție care apare atunci când încercați să deschideți un fișier care nu există, folosind un bloc
try-except.
"""
try:
    with open('readme.txt', 'r') as f:
        linesx = f.readlines()
        for line in linesx:
            print(line)
except FileNotFoundError:
    print("File doesn't exist!")