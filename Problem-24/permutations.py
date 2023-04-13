# Anton Ilic, Apr 8, 2023
# https://projecteuler.net/problem=24
# Note, I found a solution, but it was extremly slow. To speed it up, I read about the 'generation in lexical order' algorithm found here: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

def convertToList(selectedIntOrStr):
    listOfNumbers = []
    for i in selectedIntOrStr:
        listOfNumbers.append(int(i))
    return listOfNumbers

def convertToInt(selectedListOfInt):
    number = ''
    for element in selectedListOfInt:
        number += str(element)
    return int(number)

def swapElements(listOfElements, firstIndex, secondIndex):
    print(f'Swapping {firstIndex} and {secondIndex}')
    temp = listOfElements[firstIndex]
    listOfElements[firstIndex] = listOfElements[secondIndex]
    listOfElements[secondIndex] = temp
    return listOfElements

def getNextPermutation(currentPermutation):
    
    # find a[k] < a[k+1] ie. 87132 where k = [2] 
    # find largest index l where l > k, such that a[k] < a[l] ie. l is [4] 
    # swap a[k] and a[l] ie. 87132 becomes 87231
    # reverse from a[k+1] up to final element is reversed (ie. 872-[31] -> 87213

    lowestLargerThenIndex = 0 # a[k]
    largestIndexGreater = 0 # index l

    #finding pair where the next element is greater then the current
    currentPermutation = str(currentPermutation)
    for i in range(0, 8):
        if int(currentPermutation[i]) < int(currentPermutation[i+1]):
            #found pair 
            lowestLargerThenIndex = i

    for i in range(lowestLargerThenIndex - 1, 9):
        if int(currentPermutation[lowestLargerThenIndex]) < int(currentPermutation[i]):
            largestIndexGreater = i
    
    #swapping values
    currentPermutation = convertToList(currentPermutation)
    print(currentPermutation)
    currentPermutation = swapElements(currentPermutation, lowestLargerThenIndex, largestIndexGreater)
    print(currentPermutation)


    return currentPermutation

listOfCombos = []
listOfOneToTen = [*range(0, 10)]
listOfOneToTen = convertToInt(listOfOneToTen)

for i in range(1, 1000001):
    #listOfCombos.append(listOfOneToTen)
    listOfOneToTen = getNextPermutation(listOfOneToTen)

print(listOfOneToTen)

    


"""listOfCombos = []
listOfOneToTen = [*range(0, 10)]

for a in range(0, 10):
    for i in listOfOneToTen:
        for j in listOfOneToTen:
            tempElement = listOfOneToTen[i]
            listOfOneToTen[i] = listOfOneToTen[j]
            listOfOneToTen[j] = tempElement

            listOfCombos.append(convertToInt(listOfOneToTen))

"""

