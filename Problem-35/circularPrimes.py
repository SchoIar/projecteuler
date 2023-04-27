# Anton Ilic, Apr 26, 2023
# https://projecteuler.net/problem=35

import unittest


def findLenOfListOfCircularPrimes(listOfPrimes):
    circularPrimesList = []
    for prime in listOfPrimes:
        notCircularPrime = False
        primeStr = str(prime)
        for i in range(len(primeStr)):
            shifted = primeStr[i:] + primeStr[:i]  # Rotating digit by slicing
            if not isPrime(int(shifted)):
                notCircularPrime = True
                break
        if not notCircularPrime:
            circularPrimesList.append(prime)

    return len(circularPrimesList)


def possibleCircularPrimesOver100(number):
    # circular primes over 100 will only contain '1' '3' '7' and '9', and are rotations
    number = str(number)
    if ('2' in number or '4' in number or '5' in number or '6' in number or '8' in number or '0' in number):
        return False
    return True


def isPrime(number):
    if number % 2 == 0 or (number > 100 and possibleCircularPrimesOver100(number) == False):
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def solution(maxNumber):
    listOfPrimes = []
    for i in range(1, maxNumber + 1):
        if isPrime(i):
            listOfPrimes.append(i)
    return findLenOfListOfCircularPrimes((listOfPrimes))

#Unit tests
class TestCircularPrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(4))

    def test_possibleCircularPrimesOver100(self):
        self.assertTrue(possibleCircularPrimesOver100(137))
        self.assertFalse(possibleCircularPrimesOver100(102))

    def test_findLenOfListOfCircularPrimes(self):
        self.assertEqual(findLenOfListOfCircularPrimes(
            [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]), 13)
        self.assertEqual(findLenOfListOfCircularPrimes(
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]), 13)

    def test_failing_tests(self):
        # Unit tests with incorrect expected results
        self.assertFalse(isPrime(3))
        self.assertTrue(possibleCircularPrimesOver100(102))
        self.assertEqual(findLenOfListOfCircularPrimes(
            [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]), 14)


# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    circularPrimesCount = solution(1000000)
    print(
        f'Number of circular primes under and up to a million: {circularPrimesCount}')
