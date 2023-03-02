#Anton Ilic, Mar 1, 2023
#https://projecteuler.net/problem=10
#Sum of all primes under two million
def findPrime():
    primes = [2]
    i = 3
    primeSum = 2
    while(i < 2000000):
        isPrime = True
        for primeNumber in primes:
            if(i%primeNumber == 0):
                #not a prime number
                isPrime = False
        if(isPrime):
            #primes.append(i)
            primeSum += i
        i = i + 2
    return primeSum
    #primeSum = sum(primes)