"""
Creati un dictionar nou cu dict comprehension care are ca valori ultimele doua caractere ale valorilor functiilor daca
acestea sunt string.
Adica daca old_dict = {"ab": "abcde", "aaa": [1,2,3], "cd": "zyur", "sdfd": 124}
Atunci new_dict = {"ab": "de", "cd": "ur"}
"""

def last_two_chars_from_string(a_dict):
    return {x: y[-2:] for (x, y) in a_dict.items() if isinstance(y, str)}

old_dict = {"ab": "abcde", "aaa": [1,2,3], "cd": "zyur", "sdfd": 124}
print(last_two_chars_from_string(old_dict))