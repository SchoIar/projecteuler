# Anton Ilic, May 5, 2023
# https://projecteuler.net/problem=45

# Brute force method
def findTriangleNumber(key):
    return int(key * (key + 1) / 2)

def findPentagonalNumber(key):
    return int(key * ((3 * key) - 1) / 2)

def findHexogonalNumber(key):
    return int(key * (2 * key - 1))

def solution():
    currentTriNumber = 286; currentPent = 166; currentHex = 144
    triList = [findTriangleNumber(286)]; pentList = [findPentagonalNumber(currentPent)]; hexList = [findHexogonalNumber(currentHex)]
    while ((triList[len(triList) - 1] not in pentList) and (triList[len(triList) - 1] not in hexList)):

        while triList[len(triList) - 1] > pentList[len(pentList) - 1]:
            currentPent += 1
            pentList.append(findPentagonalNumber(currentPent))

        while triList[len(triList) - 1] > hexList[len(hexList) - 1]:
            currentHex += 1
            hexList.append(findHexogonalNumber(currentHex))

        currentTriNumber += 1
        triList.append(findTriangleNumber(currentTriNumber))

    return triList[len(triList) - 1]

if __name__ == '__main__':
    print(solution())
