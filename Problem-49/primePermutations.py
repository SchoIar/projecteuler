# Anton Ilic, May 13, 2023
# https://projecteuler.net/problem=49

# 4 digit increasing sequence...  (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
from itertools import permutations


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


def findPrimePermutations():

    listOfPrimes = generatePrimes()
    listOfPrimePermutations = []
    for number in listOfPrimes:
        permutationsList = permutations(str(number))
        primePermutationsList = []
        mySet = set()
        for element in permutationsList:
            stringOfElement = ''
            for thing in element:
                stringOfElement += thing
            intOfElement = int(stringOfElement)
            if isPrime(intOfElement) and len(str(intOfElement)) == 4:
                mySet.add(intOfElement)
        for element in mySet:
            if element in listOfPrimes:
                if element not in primePermutationsList:
                    primePermutationsList.append(element)

        if len(primePermutationsList) >= 3:
            if isThreeEquallySpaced(primePermutationsList) != 0:
                listOfPrimePermutations.append(primePermutationsList)
                print(primePermutationsList)
    return listOfPrimePermutations


def isThreeEquallySpaced(primesList):
    for a in primesList:
        #checking for the "middle" number, which has two equal differences 
        differencesForNumber = []
        checkedNumbers = []
        #primesList = list(dict.fromkeys(primesList))
        for b in primesList:
            if a == b:
                continue
            
            difference = abs(a - b) 
            if difference in differencesForNumber and (a not in checkedNumbers and b not in checkedNumbers):
                return difference
            checkedNumbers.append(b)
            differencesForNumber.append(difference)     
    return 0


def solution():

    #findPrimePermutations()
    primePermutationsList = findPrimePermutations()
    print(primePermutationsList)


if __name__ == '__main__':
    print(solution())
