def is_even(n):
    return n% 2==0

def factorial(n):
    if n< 0:
        raise ValueError("Negative not allowed")
    result = 1
    for i in range(2,n+1) :
        result *= i
    return result