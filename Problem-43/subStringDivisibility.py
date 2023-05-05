# Anton Ilic, May 5, 2023
# https://projecteuler.net/problem=43
import itertools


def generatePandigitalNumber():
    firstPandigitalNumber = '0123456789'
    pandigitalNumbersList = list(itertools.permutations(firstPandigitalNumber))
    newList = []
    for element in pandigitalNumbersList:
        elementStr = ''
        for thing in element:
            elementStr = elementStr + str(thing)
        newList.append(elementStr)
    return newList


def subStringDivisable(number):
    numStr = str(number)
    numList = [2, 3, 5, 7, 11, 13, 17]
    for a in range(0, 7):
        if not int(numStr[1 + a:4 + a]) % numList[a] == 0:
            return False
    return True


def solution():
    pandigitalNumbersList = generatePandigitalNumber()
    sumOfDivisibleSubstrings = 0
    for number in pandigitalNumbersList:
        if subStringDivisable(number):
            sumOfDivisibleSubstrings += int(number)
    return sumOfDivisibleSubstrings


if __name__ == '__main__':
    sum_of_divisible_substrings = solution()
    print(sum_of_divisible_substrings)
