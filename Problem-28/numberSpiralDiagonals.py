# Anton Ilic, Apr 18, 2023
# https://projecteuler.net/problem=28

def findSumOfDiagonal(listOfNumbers):
    sumOfDiagonal = listOfNumbers[500][500] * -1
    #Sum of indexes 00, 11, ... 1000 1000 plus 1000 0 999 1 ... 0 1000 [middle at 500, 500 is iterated thru twice]
    for a in range(0, 1001):
        sumOfDiagonal += listOfNumbers[a][a]
        sumOfDiagonal += listOfNumbers[a][1000-a] 
    return sumOfDiagonal

def createSpiralOfDiagonals():
    a = [[0] * 1001 for element in range(1001)] #create array to hold values

    #set middle index (500, 500) to 1, then 501,500 to 2 then 501,501 to 3 then 500, 501 to ... etc.
    x = 500; y = 500

    for nextNumber in range(1, 1001 ** 2 + 1):
        pass
    #a[x][y] = nextNum

#patern relative to center
    # +1 0
    # +1 +1
    # 0 +1
    # -1 +1
    # -1 0
    # -1 -1


createSpiralOfDiagonals()