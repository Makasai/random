"""
Tail recursion of factorial. Pass 1 as accum value
Usage: factorial(5,1)  
"""

def factorial(n, accum):
    if n == 0:
        return accum

    return factorial(n-1, accum * (n-1))
