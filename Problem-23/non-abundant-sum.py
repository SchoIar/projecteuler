# Anton Ilic, completed Apr 7, 2023
# https://projecteuler.net/problem=23

def findFactors(number):
    factors = []
    for i in range(1, number):
        if(number%i == 0):
            factors.append(i)
    return factors

def isAbundant(number):
    if sum(findFactors(number)) > number:
        return True
    else: #'perfect' number or non-abundant
        return False 

listOfNumbers = []
for i in range(1,28124):#(1, 28124):
    if(isAbundant(i)):
        listOfNumbers.append(i)

