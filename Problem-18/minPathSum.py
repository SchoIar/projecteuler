# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

def findMaxTotal(numberList):
    numberOfRows = len(numberList)
    maxSum = 0; sum = numberList[0][0]
    #00
    #10 11
    #20 21 22 
    #30 31 32 33
    print(numberList[numberOfRows-1][len(numberList[numberOfRows-1])-1])#print the last number

    for i in range(0,15):
        #adds to zeroth path
        sum += numberList[i][0]



    return numberOfRows

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)

findMaxTotal(numbers)