# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=37

import unittest

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def isTruncablePrime(number):
    if number < 10 or not isPrime(number):  # single digit numbers and non-primes aren't truncatable primes
        return False

    #Check if Truncable, and if previously found .. 
    return True



def solution():
    truncatable_primes = []
    i = 11  #single digits are not truncable
    while len(truncatable_primes) < 11:  # 11 such truncatable primes.
        if isTruncablePrime(i):
            truncatable_primes.append(i)
        i += 2  # only check odd numbers
    return sum(truncatable_primes)


class TestTruncatablePrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(13))

    def test_isTruncablePrime(self):
        self.assertFalse(isTruncablePrime(120))
        self.assertTrue(isTruncablePrime(3797))
        


# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(solution())

