# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

def findnewMaxLayer(numberList):
    ''''Returns new 'bottom' layer by finding maximum values from other layers'''
    #return numberList.pop(len(numberList)-1)

def findMaxSum(numberList):
    '''Finds optimal path's sum by finding maximum sum by 'layer'.'''
    numberOfRows = len(numberList)
    if(numberOfRows == 1):
        print(numberList)
        return numberList[0][0]
    else:
        findnewMaxLayer(numberList)

    findMaxSum(numberList)

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)

findMaxSum(numbers)