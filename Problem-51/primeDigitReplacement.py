# Anton Ilic, May 17, 2023
# https://projecteuler.net/problem=51

from itertools import combinations


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def replaceNumberIndex(number, index, value):
    number = list(str(number))
    number[index] = value
    currentString = ''
    for element in number:
        currentString += str(element)
    return currentString


def replaceDigits(number):
    primesSet = set()
    numberStr = str(number)
    # TODO: iterate through all possible replacement digits - not just the Nth digit
    for digit in range(0, len(numberStr)):
        primesSet = set()
        for replacementDigit in range(0, 10):
            # for 1 digit..
            currentString = replaceNumberIndex(number, digit, replacementDigit)

            if isPrime(int(currentString)):
                if not currentString[0] == '0':
                    primesSet.add(int(currentString))
                    print(currentString)

            if len(primesSet) == 8:
                return min(primesSet)


def main():
    start = 3
    while True:
        start += 2
        if isPrime(start):
            potentialSolution = replaceDigits(start)
            if potentialSolution != None:
                return potentialSolution


if __name__ == '__main__':

    solution = main()
    print(solution)
