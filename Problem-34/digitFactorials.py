# Anton Ilic, Apr 25, 2023
# https://projecteuler.net/problem=34

# Function to calculate the factorial of a given number
def factorial(element):
    fsum = 1
    for i in range(1, element + 1):
        fsum = fsum * i  
    return fsum  

# Function to check if the sum of the factorials of the digits of a number is equal to the number itself
def isDigitsEqualToFactorial(number):
    numberStr = str(number) 
    factorialSum = 0 

    for element in numberStr:
        # Add the factorial of the digit to the sum of factorials
        factorialSum += factorial(int(element))

    if(number == factorialSum):
        return True  #
    return False  

# Function to find the sum of numbers that satisfy the isDigitsEqualToFactorial condition up to a given maximum number
def solution(maxNumber):
    '''Finds all cases where the digits of the number as factorials are equal to the number'''
    sumOfDigitsEqualToFactorial = 0 
    for currentNumber in range(3, maxNumber):
        if isDigitsEqualToFactorial(currentNumber) == True:
            sumOfDigitsEqualToFactorial += currentNumber
    return sumOfDigitsEqualToFactorial 

# Entry point of the script
if __name__ == '__main__':
    # Since 9999999 > 9! * 7, all greater numbers will be smaller than their sum of digit factorials
    print(solution(factorial(9) * 7))  
