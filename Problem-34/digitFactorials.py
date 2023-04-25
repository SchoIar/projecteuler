# Anton Ilic, Apr 24, 2023
# https://projecteuler.net/problem=34
def factorial(element):
    fsum = 1
    for i in range(1, element + 1):
        fsum = fsum * i
    return fsum

def isDigitsEqualToFactorial(number):
    numberStr = str(number)
    factorialSum = 0
    for element in numberStr:
        factorialSum += factorial(int(element))
    if(number == factorialSum):
        return True
    else:
        print(f'{numberStr} is the original, {factorialSum} is sum')
  
#TODO: Figure out what maxNumber is- when does the factorial of digits become smaller then the numbe.. know that 9! is 362880
def solution(maxNumber):
    '''Finds all cases where the digits of the number as factorials are equal to the number'''
    sumOfDigitsEqualToFactorial = 0
    for currentNumber in range(3, maxNumber):
        if isDigitsEqualToFactorial(currentNumber) == True:
            sumOfDigitsEqualToFactorial += currentNumber
    return sumOfDigitsEqualToFactorial

# Entry point of the script
if __name__ == '__main__':
    print(solution(99999))