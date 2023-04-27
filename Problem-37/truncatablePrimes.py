# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=37

import unittest

def isTruncablePrime(number):
    numStr = str(number)
    
    

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

class TestTruncatablePrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(13))


# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

