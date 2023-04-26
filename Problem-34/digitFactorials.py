# Anton Ilic, Apr 25, 2023
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
    return False
  

def solution(maxNumber):
    '''Finds all cases where the digits of the number as factorials are equal to the number'''
    sumOfDigitsEqualToFactorial = 0
    for currentNumber in range(3, maxNumber):
        if isDigitsEqualToFactorial(currentNumber) == True:
            sumOfDigitsEqualToFactorial += currentNumber
    return sumOfDigitsEqualToFactorial

# Entry point of the script
if __name__ == '__main__':
    #Since 9999999 > 9! * 7... all greater then will be smaller then 
    print(solution(factorial(9) * 7)) #9! * 7