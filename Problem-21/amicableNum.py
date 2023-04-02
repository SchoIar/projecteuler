# Anton Ilic, completed Apr 1, 2023
# https://projecteuler.net/problem=21

def findDivisorsSum(number):
    divisorSum = 0
    for i in range(1, number):
        if(number%i == 0):
            divisorSum += i
    return divisorSum

def findAmicableNumbersSum():
    sumOfAmicableNumbers = 0
    for i in range(1, 10000):
        divisorSum = findDivisorsSum(i)
        if findDivisorsSum(divisorSum) == i and divisorSum != i:
            sumOfAmicableNumbers += i
    return sumOfAmicableNumbers

print(findAmicableNumbersSum())

