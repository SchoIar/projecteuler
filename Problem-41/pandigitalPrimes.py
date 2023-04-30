# Anton Ilic, Apr 29, 2023
# https://projecteuler.net/problem=41
import unittest

def isPrime(number):
    for num in range(2, int(number**0.5) + 1):
        if number % num == 0:
            return False
    return True

def isPandigitalToNThDigit(number):
    lengthOfNumber = len(str(number))
    if lengthOfNumber > 9:
        return False
    for digit in range(1, lengthOfNumber + 1):
        if str(digit) in str(number):
            pass
        else:
            return False
    return True

def isPandigitalPrime(number):
    if isPandigitalToNThDigit(number) and isPrime(number):
        return True
    else:
        return False

def solution():
    for number in range(987654321 + 1, 1, -2):
        if isPandigitalPrime(number):
            return number
class TestPandigitalPrimes(unittest.TestCase):
    def test_isPandigitalToNThDigit(self):
        self.assertTrue(isPandigitalToNThDigit(123))
    
    def test_isPrime(self):
        self.assertTrue(isPrime(13))
        self.assertFalse(isPrime(21321))

    def test_isPandigitalPrime(self):
        isPandigitalPrime(2143)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    largestPandigitalPrime = solution()
    print(largestPandigitalPrime)