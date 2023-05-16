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
        permutationsList = list(dict.fromkeys(permutationsList))
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

            permutationWithDifference = find_seq_with_same_diff(primePermutationsList)
            if permutationWithDifference != None and permutationWithDifference not in listOfPrimePermutations:
                listOfPrimePermutations.append(permutationWithDifference)

    return listOfPrimePermutations



def find_seq_with_same_diff(listOfPrimePermutations):
    listOfPrimePermutations.sort()

    lengthOfList = len(listOfPrimePermutations)
    for i in range(lengthOfList):
        for j in range(i+1, lengthOfList):
            if 2*listOfPrimePermutations[j] - listOfPrimePermutations[i] in listOfPrimePermutations[j+1:]:
                # Check if the number with the same difference exists in the rest of the list
                return str(listOfPrimePermutations[i]) + str(listOfPrimePermutations[j]) + str(2*listOfPrimePermutations[j] - listOfPrimePermutations[i])
    return None


if __name__ == '__main__':
    solutions = findPrimePermutations()
    print(solutions)
