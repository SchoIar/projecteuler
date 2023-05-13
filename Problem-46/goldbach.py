# Anton Ilic, May 12, 2023
# https://projecteuler.net/problem=46

# Odd composite numbers (all the odd integers that are not prime).

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isGoldbachNumber(listOfPrimes, number):
    for prime in listOfPrimes:
        if prime < number:
            composite = ((number - prime) / 2) ** 0.5
            if composite == int(composite):
                return True
        else:
            return False


def solution():
    primesList = []
    currentNumber = 9
    for i in range(2, currentNumber):
        if isPrime(i):
            primesList.append(i)

    while True:
        if isPrime(currentNumber):
            primesList.append(currentNumber)
        else:
            if not isGoldbachNumber(primesList, currentNumber):
                return currentNumber
        currentNumber += 2  # only iterate through even numbers


if __name__ == '__main__':
    goldbachNumber = solution()
    print(goldbachNumber)
