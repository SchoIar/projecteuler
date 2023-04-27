# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=36

import unittest

def isDecimalPalindrome(number):
    numStr = str(number)
    return numStr == numStr[::-1]

def isBinaryPalindrome(number):
    binaryNum = ''
    while number != 0:
        if (number // 2 == number / 2):
            binaryNum = binaryNum + '0'
        else:
            binaryNum = binaryNum + '1'
        number = number // 2
    return isDecimalPalindrome(int(binaryNum[::-1])) #Converting to int to remove leading 0s
    

def isDoublePalindrome(number):
    if isDecimalPalindrome(number):
        if isBinaryPalindrome(number):
            return True
    return False
    

def solution(maxNumber):
    sumOfDoubleDigitPalindromes = 0
    for number in range(1, maxNumber + 1):
        if isDoublePalindrome(number):
            sumOfDoubleDigitPalindromes += number
    return sumOfDoubleDigitPalindromes

class TestCircularPrimes(unittest.TestCase):
    def test_isDecimalPalindrome(self):
        self.assertFalse(isDecimalPalindrome(81))
        self.assertTrue(isDecimalPalindrome(8187818))
        self.assertTrue(isDecimalPalindrome(777))
        self.assertFalse(isDecimalPalindrome(7797))
    
    def test_isBinaryPalindrome(self):
        self.assertFalse(isBinaryPalindrome(2))
        self.assertTrue(isBinaryPalindrome(585))

    def test_isDoublePalindrome(self):
        self.assertTrue(isDoublePalindrome(585))

# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    sumOfAMillionDoublePrimes = solution(1000000)
    print(f'Sum of a million double palindromes: {sumOfAMillionDoublePrimes}')


