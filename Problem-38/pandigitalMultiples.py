# Anton Ilic, Apr 28, 2023
# https://projecteuler.net/problem=38

import unittest

def is_Pandigital(number):
    numStr = str(number)
    if len(numStr) != 9:
        return False
    for i in range(1, 10):
        if str(i) in numStr:
            pass
        else:
            return False
    return True
    

def findPandigitalNumber(intialNumber, maxNumber):
    pandigitalNumber = ''
    for i in range(1, maxNumber + 1):
        pandigitalNumber += str(i * intialNumber)
    return int(pandigitalNumber)

def solution():
    max_pandigital = 0
    for initial_number in range(1, 10000):
        n = 1
        currentProduct = ''
        while(len(currentProduct) < 9):
            currentProduct += str(initial_number * n)
            n += 1
        
        if(is_Pandigital(currentProduct)):
            max_pandigital = str(max(int(max_pandigital), int(currentProduct)))

    return max_pandigital

class TestPandigitalNumbers(unittest.TestCase):
    def test_findPandgitalNumber(self):
        self.assertTrue(findPandigitalNumber(1, 3) == 123)

    def test_isPandigital(self):
        self.assertTrue(is_Pandigital(123456789))
        self.assertTrue(is_Pandigital(123456897))
        self.assertFalse(is_Pandigital(1122334560897))
        self.assertFalse(is_Pandigital(12344567890))

# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(solution())
