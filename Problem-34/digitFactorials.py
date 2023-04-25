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
  
    
# Entry point of the script
if __name__ == '__main__':
    pass