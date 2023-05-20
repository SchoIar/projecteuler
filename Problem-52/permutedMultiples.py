# Anton Ilic, May 18, 2023
# https://projecteuler.net/problem=52

def isDigitsOfAInB(alpha, beta):
    strAlpha = str(alpha)
    strBeta = str(beta)
    if len(strAlpha) != len(strBeta):
        return False
    for digit in strAlpha:
        if not digit in strBeta:
            return False
    return True


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
    # TODO: Check for number of digits occurance, if equal, isDigitOfAInB should return true - if not - return a problem.
    # not a problem to get the correct solution for this problem.
    # ie, (isDigitsOfAInB(1123, 3221)) would be True
    solution = main()
    print(solution)
