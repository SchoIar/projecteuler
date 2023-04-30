# Anton Ilic, Apr 29, 2023
# https://projecteuler.net/problem=40

def createConcatNumber():
    concatenationAfterDecimal = ''
    for a in range(1, 1000000):
        concatenationAfterDecimal = str(concatenationAfterDecimal) + str(a)
    return concatenationAfterDecimal

def solution():
    pass

if __name__ == '__main__':
    pass