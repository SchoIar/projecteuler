# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=37

import unittest

def isTruncablePrime(number):
    pass
    
def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(number):
    listOfTruncablePrimes = []
    
    #loop to find truncable primes list.. Note that they must be composed without '2' '4' '5' '6' '8' '9' '0' within the digits

class TestTruncatablePrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(13))


# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

