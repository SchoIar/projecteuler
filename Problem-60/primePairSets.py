# Anton Ilic, May 31, 2023
# https://projecteuler.net/problem=60

def isPrime(number):
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def isCombinationsPrime(listOfNumbers):
    for firstNumber in listOfNumbers:
        for secondNumber in listOfNumbers:
            strFirstNum = str(firstNumber)
            strSecondNum = str(secondNumber)
            if firstNumber == secondNumber:
                continue
            combinedNumber = strFirstNum + strSecondNum
            if not isPrime(int(combinedNumber)):
                return False
    return True

def isCombinationPrime(a, b):
    return (isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a))))

def generateNPrimes(start, end):
    primesList = []
    for i in range(start, end + 1):
        if isPrime(i):
            primesList.append(i)
    return primesList

