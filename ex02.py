
"""Scrieți o expresie regulată pentru a valida un "Nume Prenume" (trebuie sa fie doua cuvinte,
ambele sa inceapa cu majuscula. Ignorati prenumele complexe)"""
import re
regex = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
def validate_name_prenume(nume_intreg):
    if re.match(regex, nume_intreg):
        print("Nume Prenume valid.")
    else:
        print("Nume Prenume invalid.")
validate_name_prenume("Ion Iliescu")  # Valid
validate_name_prenume("gica popescu")    # Invalid (nu începe cu majusculă)
validate_name_prenume("Maria Tuica")   # Valid
validate_name_prenume("liviu dorobantu")    # Invalid (nu începe cu majusculă)
validate_name_prenume("Vasile Mai-Vasile")  # Invalid (prenume complex)