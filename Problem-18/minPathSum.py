# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

def backTrack(numberList):
    '''Backtracks to root, to find sum of paths,'''
    numberOfRows = len(numberList)
    maxSum = 0; sum = numberList[0][0]
    print(numberList[numberOfRows-1][len(numberList[numberOfRows-1])-1])#print the last number

    
    return numberOfRows

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)

backTrack(numbers)