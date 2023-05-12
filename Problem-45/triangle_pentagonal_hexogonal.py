# Anton Ilic, May 5, 2023
# https://projecteuler.net/problem=45
import unittest
# Brute force method
def findTriangleNumber(key):
    return int(key * (key + 1) / 2)


def findPentagonalNumber(key):
    return int(key * ((3 * key) - 1) / 2)


def findHexogonalNumber(key):
    return int(key * (2 * key - 1))


def solution(current_triangle_index, current_pentagonal_index, current_hexogonal_index):
    '''Returns a tuple of the Triangle number's 'n' value, and the triangle number, which is also a hexogonal and pentagonal number'''
    triangleNumberList = []
    pentagonalNumberList = [findPentagonalNumber(current_pentagonal_index)]
    hexogonalNumberList = [findHexogonalNumber(current_hexogonal_index)]
    while True:
        maxTriangleNumber = findTriangleNumber(current_triangle_index)
        triangleNumberList.append(maxTriangleNumber)

        # Appending pentagonal numbers up untill greater then max triangle number
        while (pentagonalNumberList[len(pentagonalNumberList) - 1] <= maxTriangleNumber):
            current_pentagonal_index += 1
            pentagonalNumberList.append(
                findPentagonalNumber(current_pentagonal_index))

        # Appending hexagonal numbers up untill greater then max triangle number
        while (hexogonalNumberList[len(hexogonalNumberList) - 1] <= maxTriangleNumber):
            current_hexogonal_index += 1
            hexogonalNumberList.append(
                findHexogonalNumber(current_hexogonal_index))

        if maxTriangleNumber in pentagonalNumberList and maxTriangleNumber in hexogonalNumberList:
            # returning the triangle number which is also pent. and hexo.
            return maxTriangleNumber

        current_triangle_index += 1


class TestEulerProblem(unittest.TestCase):
    def test_findTriangleNumber(self):
        self.assertEqual(findTriangleNumber(1), 1)
        self.assertEqual(findTriangleNumber(2), 3)
        self.assertEqual(findTriangleNumber(3), 6)
        self.assertEqual(findTriangleNumber(4), 10)

    def test_findPentagonalNumber(self):
        self.assertEqual(findPentagonalNumber(1), 1)
        self.assertEqual(findPentagonalNumber(2), 5)
        self.assertEqual(findPentagonalNumber(3), 12)
        self.assertEqual(findPentagonalNumber(4), 22)

    def test_findHexogonalNumber(self):
        self.assertEqual(findHexogonalNumber(1), 1)
        self.assertEqual(findHexogonalNumber(2), 6)
        self.assertEqual(findHexogonalNumber(3), 15)
        self.assertEqual(findHexogonalNumber(4), 28)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
    print(solution(286, 165, 143))
