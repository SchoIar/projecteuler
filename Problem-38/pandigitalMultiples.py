# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=38
import unittest
def findPandigitalNumber(intialNumber, maxNumber):
    pandigitalNumber = ''
    for i in range(1, maxNumber + 1):
        pandigitalNumber += str(i * intialNumber)
    return int(pandigitalNumber)

def solution(number):
    '''Finds the largest nine digit pandigital 9 digit number where n > 1 where.. the number is ABC * 1... ABC * n'''
    pass

class TestPandigitalNumbers(unittest.TestCase):
    def test_findPandgitalNumber(self):
        self.assertTrue(findPandigitalNumber(1, 3) == 123)

# Entry point of the script
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)