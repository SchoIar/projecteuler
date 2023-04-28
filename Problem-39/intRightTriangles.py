# Anton Ilic, Apr 28, 2023
# https://projecteuler.net/problem=39

import unittest
## Perimiter = a + b + c... Number of solutions maximized..
def findNumberOfSolutions(perimeter):
    
    solutions = {}

    #Body of code, find solutions, append them to solutions.
    for a in range(1, perimeter + 1):
        for b in range(1, perimeter + 1):
            c = (a**2 + b**2) ** 0.5
            if a + b + c == perimeter:
                maxNum = max(a,b); minNum = min(a, b)
                solutions[(minNum, maxNum)] = c            

    return len(solutions)

def solution():
    maxSolution = (0, 0) #Tuple in form (Number of solutions : Perimeter)
    for perimeter in range(1, 1001):
        print(perimeter)
        numberOfSolutionsForSelectedPerimeter = findNumberOfSolutions(perimeter)
        if numberOfSolutionsForSelectedPerimeter > maxSolution[0]:
            maxSolution = (numberOfSolutionsForSelectedPerimeter, perimeter)
    return maxSolution[1]

class TestPandigitalNumbers(unittest.TestCase):
    def test_findNumberOfSolutions(self):
        self.assertEqual(findNumberOfSolutions(120), 3)

if __name__ == '__main__':
    #unittest.main(argv=[''], exit=False)
    print(solution())