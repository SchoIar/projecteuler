# Anton Ilic, Apr 8, 2023
# https://projecteuler.net/problem=24

def convertToInt(selectedListOfInt):
    number = ''
    for element in selectedListOfInt:
        number += str(element)
    return int(number)

def swap(array, indexOne, indexTwo):
    '''Swaps array indicies One and Two'''
    temp = array[indexOne]
    array[indexOne] = array[indexTwo]
    array[indexTwo] = temp
    return array

def getSortedArray():
    #sort in order here, return millionth element 
    pass
    


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

