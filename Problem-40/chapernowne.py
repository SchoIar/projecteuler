# Anton Ilic, Apr 29, 2023
# https://projecteuler.net/problem=40

def createConcatNumber():
    concatenationAfterDecimal = ''
    for a in range(1, 1000000):
        concatenationAfterDecimal = str(concatenationAfterDecimal) + str(a)
    return concatenationAfterDecimal

def solution():
    concatNum = createConcatNumber()
    product = 1
    for number in range(0, 7):
        product = product * int(concatNum[10**number - 1])
    return product

if __name__ == '__main__':
    print(solution())