# Anton Ilic, May 17, 2023
# https://projecteuler.net/problem=51

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True