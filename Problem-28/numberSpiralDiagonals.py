# Anton Ilic, Apr 18, 2023
# https://projecteuler.net/problem=28

def findSumOfDiagonal(listOfNumbers):
    sumOfDiagonal = listOfNumbers[500][500] * -1
    #Sum of indexes 00, 11, ... 1000 1000 plus 1000 0 999 1 ... 0 1000 [middle at 500, 500 is iterated thru twice]
    for a in range(0, 1001):
        sumOfDiagonal += listOfNumbers[a][a]
        sumOfDiagonal += listOfNumbers[a][1000-a] 
    return sumOfDiagonal

#Generates the 1001 x 1001 spiral
def createSpiralOfDiagonals(spiralSize):
    the2Darray = [[0] * spiralSize for element in range(1001)] #create array to hold values

    #set middle index (500, 500) to 1, then 501,500 to 2 then 501,501 to 3 then 500, 501 to ... etc.
    x = spiralSize // 2; y = spiralSize // 2
    
    for nextNumber in range(1, spiralSize ** 2 + 1):
        
        the2Darray[x][y] = nextNumber
        
        exit()
    #a[x][y] = nextNum

#patern relative to center
    # +1 0
    # +1 +1
    # 0 +1
    # -1 +1
    # -1 0
    # -1 -1


createSpiralOfDiagonals(1001)