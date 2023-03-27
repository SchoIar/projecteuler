# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

def findnewMaxLayer(numberList):
    ''''Returns new 'bottom' layer by finding maximum values from other layers'''
    #TODO: Add code to 'condense' bottom two rows, and replace index len-2 w it.

    newList = []
    number = 0
    for i in numberList[len(numberList)-2]:
        numberToAdd = i + numberList[len(numberList)-1][number+1]#max(numberList[len(numberList)-1][number],numberList[len(numberList-1)][number+1])
        secondNumberToAdd = i + numberList[len(numberList)-1][number]
        number += 1
        newList.append(max(numberToAdd, secondNumberToAdd))

    #numberList[len(numberList)-1] = newList

    numberList.pop(len(numberList)-2)
    numberList.pop(len(numberList)-1)
    numberList.append(newList)
    return numberList

def findMaxSum(numberList):
    '''Finds optimal path's sum by finding maximum sum by 'layer'.'''

    if(len(numberList) == 1):
        print(numberList)
        return numberList
    else:
        #print(numberList)
        numberList = findnewMaxLayer(numberList)

    findMaxSum(numberList)

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)

findMaxSum(numbers)
