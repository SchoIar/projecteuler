# Anton Ilic, Apr 21, 2023
# https://projecteuler.net/problem=30


#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def findFifthPowerSumNumbers():
    listOfNumbers = []
    #chosen to iterate up to a number that I am certain cannot be summed by digits (ie. 9 ** 5 + 9 **5 + 9 ** 5 + 9 **5 + 9 ** 5 + 9 ** 5 = 354294 which is certainly less then 999999)
    for number in range(1, 354294):
        numberStr = str(number)
        sumOfDigits = 0
        for digit in numberStr:
            sumOfDigits += int(digit) ** 5
        if(sumOfDigits == number):
            listOfNumbers.append(number)
    return sum(listOfNumbers) - 1 #as noted in problem statement, '1' is not a sum

print(findFifthPowerSumNumbers())



