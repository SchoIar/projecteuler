# Anton Ilic, May 16, 2023
# https://projecteuler.net/problem=50

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(maxNumber):
    primesList = []
    for i in range(2, maxNumber + 1):
        if isPrime(i):
            primesList.append(i)
    maxPrimeSumPrime = 0
    #possible sums are at the end of primeList.. iterate through them to see if possible to be created 
    #with other numbers in primelist

    return max(primesList)

if __name__ == '__main__':
    solution = solution(1000000)
    print(solution)