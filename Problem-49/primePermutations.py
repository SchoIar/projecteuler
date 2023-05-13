# Anton Ilic, May 13, 2023
# https://projecteuler.net/problem=49

#4 digit increasing sequence...  (i) each of the three terms are prime, and, 
#(ii) each of the 4-digit numbers are permutations of one another.
import itertools

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generatePrimes():
    '''Generates a list of all primes with 4 digits'''
    primesList = []
    for i in range(1000, 10000):
        if isPrime(i):
            primesList.append(i)
    return primesList