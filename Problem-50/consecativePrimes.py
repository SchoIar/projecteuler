# Anton Ilic, May 16, 2023
# https://projecteuler.net/problem=50

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def findSumOfPrimes(primeSet):
    highestLengthPrime = 0
    maxPrimeLength = 0
    primeList = sorted(list(primeSet))  # set is unordered
    max_prime = max(primeList)
    for prime in range(0, len(primeList) - 1):
        primeSum = 0
        nextPrimeIndex = prime
        while primeSum < max_prime:
            primeSum += primeList[nextPrimeIndex]
            nextPrimeIndex += 1
            # checking lenth of chain, if larger this is the one w the highest length prime
            if primeSum in primeSet and nextPrimeIndex - prime > maxPrimeLength:
                maxPrimeLength = nextPrimeIndex - prime
                highestLengthPrime = primeSum
    return highestLengthPrime


def solution(maxNumber):
    primesSet = set()
    for i in range(2, maxNumber + 1):
        if isPrime(i):
            primesSet.add(i)
    return findSumOfPrimes(primesSet)


if __name__ == '__main__':
    solution = solution(1000000)
    print(solution)
