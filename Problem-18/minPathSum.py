# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

def findMaxTotal(numberList):
    numberOfRows = len(numberList)

    #00
    #10 11
    #20 21 22 
    #30 31 32 33
    


    return numberOfRows

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)

