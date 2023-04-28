# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=37

import unittest
    
def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def isTruncablePrime(number):
    numStr = str(number)
    if ('2' or '4' or '5' or '6' or '8' or '9' or '0') in numStr:
        return False
    elif not isPrime(number):
        return False
    
    numStr = str(number); reversedNumStr = str(number)

    while(True):
        reversedNumStr = reversedNumStr[0:len(reversedNumStr) - 1:1]
        numStr = numStr[1::]
        
        if reversedNumStr == '' or numStr == '':
            break

        if isPrime(int(numStr)):
            if isPrime(int(reversedNumStr)):
                continue
            else:
                return False
        else:
            return False
            
    return True


def solution(number):
    listOfTruncablePrimes = []
    
    
    #loop to find truncable primes list.. Note that they must be composed without '2' '4' '5' '6' '8' '9' '0' within the digits

class TestTruncatablePrimes(unittest.TestCase):
    def test_isPrime(self):
        self.assertFalse(isPrime(100))
        self.assertTrue(isPrime(13))

    def test_isTruncablePrime(self):
        self.assertFalse(isTruncablePrime(120))
        self.assertTrue(isTruncablePrime(3797))
        


# Entry point of the script
if __name__ == '__main__':
    isTruncablePrime(123456789)
    unittest.main(argv=[''], exit=False)

