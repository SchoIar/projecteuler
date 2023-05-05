# Anton Ilic, May 4, 2023
# https://projecteuler.net/problem=43
import itertools

def generatePandigitalNumber():
    pandigitalNumbers = []
    for n in range(1, 10):
        for p in itertools.permutations(range(1, n + 1)):
            num = ''
            for element in p:
                num = num + str(element)
            pandigitalNumbers.append(int(num))
    return pandigitalNumbers