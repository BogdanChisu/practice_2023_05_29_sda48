"""
Scrieti un decorator care măsoară timpul de execuție al unei funcții (hint: cu time.perf_counter())
"""

from time import perf_counter

def performance_measure(func):
    def wrapper(*args):
        start_time = perf_counter()
        rezultat = func(*args)
        took_time = perf_counter() - start_time
        print(f"Functia a luat {round(took_time,5)} secunde")
        return rezultat
    return wrapper

@performance_measure
def fibonacci_recurent(n):
    if not isinstance(n,int) or n<=0:
        return None
    if n in (1,2):
        return 1
    return fibonacci_recurent(n-1)+fibonacci_recurent(n-2)

# print(fibonacci_recurent(20))

@performance_measure
def fibonacci_2nd_solution(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci_recurent(10))
print(fibonacci_2nd_solution(1000))