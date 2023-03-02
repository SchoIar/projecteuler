# Anton Ilic, Mar 1, 2023
# https://projecteuler.net/problem=10
# Sum of all primes under two million
def findPrime():
    primes = [2]
    i = 3
    
    while (i < 2000000):
        isPrime = True
        for primeNumber in primes:
            if (i % primeNumber == 0):
                # not a prime number
                isPrime = False
        if (isPrime):
            primes.append(i)

        i = i + 2
    return sum(primes)
    #primeSum = sum(primes)

#Note: This will give the right answer? but is super slow (20+m) May try to optimize later. 

print(findPrime())
