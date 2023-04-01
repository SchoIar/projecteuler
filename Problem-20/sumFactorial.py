# Anton Ilic, completed Apr 1, 2023
# https://projecteuler.net/problem=20

def findDigitsOfFactorialSum(num):
    digits = 1; sumOfDigits = 0
    for i in range(1, num + 1):
        digits *= i

    for digit in str(digits):
        sumOfDigits += int(digit)

    return(sumOfDigits)

print(findDigitsOfFactorialSum(100))