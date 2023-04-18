# Anton Ilic, Apr 16, 2023
# https://projecteuler.net/problem=27

def isPrime(number):
    for i in range(2, number):
        if(number%i == 0):
            return False
    return True

def findMaxPrimesForNum(a, b):
    i = 1
    while isPrime(i**2 + a * i + b):
        i += 1
    return i


# n^2 + an + b, where |a| < 1000 and |b| ≤ 1000