# Anton Ilic, Apr 8, 2023
# https://projecteuler.net/problem=24
# Note, I found a solution, but it was extremly slow. To speed it up, I read about the 'generation in lexical order' algorithm found here: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

def convertToInt(selectedListOfInt):
    number = ''
    for element in selectedListOfInt:
        number += str(element)
    return int(number)


def getNextPermutation(currentPermutation):
    
    # find a[k] < a[k+1] ie. 87132 where k = [2] 
    # find largest index l where l > k, such that a[k] < a[l] ie. l is [4] 
    # swap a[k] and a[l] ie. 87132 becomes 87231
    # reverse from a[k+1] up to final element is reversed (ie. 872-[31] -> 87213
    

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

