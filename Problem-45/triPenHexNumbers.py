# Anton Ilic, May 5, 2023
# https://projecteuler.net/problem=45

# Brute force method
def findTriangleNumber(key):
    return (key * (key + 1) / 2)

def findPentagonalNumber(key):
    return (key * ((3 * key) - 1) / 2)

def findHexogonalNumber(key):
    return (key * (2 * key - 1))

'''def findNextTriangleNumber(memo):
    maxIndex = len(memo) - 1
    maxValue = memo[maxIndex]
    key = maxValue[0]
    memo.append((key, findNextTriangleNumber(key)))
    return memo
'''
'''def solution():
    triangleNumbersList = [(1, 1)]; pentagonalNumbersList = [(1, 1)]; hexagonalNumbersList = [(1, 1)]
    maxNum = triangleNumbersList[len(triangleNumbersList) - 1] 
    while(maxNum[0] < 9):
        triangleNumbersList = findNextTriangleNumber(triangleNumbersList)
    return triangleNumbersList'''

if __name__ == '__main__':
    
    '''a = solution()
    print(a)'''
    
