def findGCD(a, b):
    if a % b == 0:
        return b
    return findGCD(b, a % b)


# George's improvement
def findGCD0(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b
