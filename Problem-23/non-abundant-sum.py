# Anton Ilic, completed Apr 7, 2023
# https://projecteuler.net/problem=23
MAXVALUE = 28123
def CalculateAbundantList():
    listOfNumbers = []
    for i in range(12,MAXVALUE+1):#(1, 28124):
        if(isAbundant(i)):
            listOfNumbers.append(i)
    return listOfNumbers

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

def findSumOfValues():
    listOfSums = []
    listOfAbundants = CalculateAbundantList()
    print('CALLED FINDSUMOFVALUES')
    for firstNumber in listOfAbundants:
        for secondNumber in listOfAbundants: 
            sumOfAbundants = firstNumber + secondNumber
            if sumOfAbundants > MAXVALUE:
                break
            else:
                listOfSums.append(sumOfAbundants)
    sumOfValues = 0
    print('COMPLILING LIST')
    listOfNumbers = [*range(0, MAXVALUE+1)]
    l = list(set(listOfNumbers) - set(listOfSums))
    return sum(l)

print(findSumOfValues())
