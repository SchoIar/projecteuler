# Anton Ilic, May 16, 2023
# https://projecteuler.net/problem=50

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findSumOfPrimes(primeList):
    #find prime under max prime which can be written as the sum of the most consecutive primes
    highestLengthPrime = 0; maxPrimeLength = 0
    for prime in range(0, len(primeList) - 1):
        primeSum = 0; nextPrimeIndex = prime
        while(primeSum < max(primeList)):
            primeSum += primeList[nextPrimeIndex]
            nextPrimeIndex += 1

            if primeSum in primeList and nextPrimeIndex - prime > maxPrimeLength:
                maxPrimeLength = nextPrimeIndex - prime
                highestLengthPrime = primeSum

    return highestLengthPrime




def solution(maxNumber):
    primesList = []
    for i in range(2, maxNumber + 1):
        if isPrime(i):
            primesList.append(i)
    print(primesList)
    maxPrimeSumPrime = findSumOfPrimes(primesList)

    return maxPrimeSumPrime

if __name__ == '__main__':
    #solution = solution(1000000)
    solution = solution(100)
    print(solution)