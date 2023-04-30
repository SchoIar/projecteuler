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

class TestPandigitalPrimes(unittest.TestCase):
    def test_isPandigitalToNThDigit(self):
        self.assertTrue(isPandigitalToNThDigit(123))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    pass