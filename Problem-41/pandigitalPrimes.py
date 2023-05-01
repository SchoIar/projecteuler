# Anton Ilic, Apr 29, 2023
# https://projecteuler.net/problem=41
import unittest
import itertools

def isPrime(number):
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            return False
    return True

def generatePandigitalNumber():
    pandigitalNumbers = []
    for n in range(1, 10):
        for p in itertools.permutations(range(1, n + 1)):
            num = ''
            for element in p:
                num = num + str(element)
            pandigitalNumbers.append(int(num))
    return pandigitalNumbers

def solution():
    listOfPandigitalNumbers = generatePandigitalNumber()
    for number in range(len(listOfPandigitalNumbers) - 1, 0, -1):
        pandigital_number = listOfPandigitalNumbers[number]
        if isPrime(pandigital_number):
            return pandigital_number

class TestPandigitalPrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertTrue(isPrime(13))
        self.assertFalse(isPrime(21321))

if __name__ == '__main__':
    #unittest.main(argv=[''], exit=False)
    largestPandigitalPrime = solution()
    print(largestPandigitalPrime)
