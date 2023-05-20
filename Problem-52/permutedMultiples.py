# Anton Ilic, May 19, 2023
# https://projecteuler.net/problem=52

def numberOfDigits(number):
    digitList = {}
    for digit in str(number):
        if digit in digitList:
            digitList[digit] += 1
        else:
            digitList[digit] = 1
    return digitList


def isDigitsOfAInB(alpha, beta):
    '''True if all digits of 'alpha' are in 'beta' otherwise False '''
    strAlpha = str(alpha)
    strBeta = str(beta)
    if len(strAlpha) != len(strBeta):
        return False
    return numberOfDigits(strAlpha) == numberOfDigits(strBeta)


def arePermutedMultiples(number):
    for multipleOfNumber in range(2, 7):
        currentMultiple = multipleOfNumber * number
        if not isDigitsOfAInB(number, currentMultiple):
            return False
    return True


def main():
    start = 1
    while True:
        if arePermutedMultiples(start):
            return start
        start += 1


if __name__ == '__main__':
    solution = main()
    print(solution)
