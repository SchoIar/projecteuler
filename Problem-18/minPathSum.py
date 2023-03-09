# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)
print(numbers)