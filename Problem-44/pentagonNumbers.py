# Anton Ilic, May 5, 2023
# https://projecteuler.net/problem=44

# PenNum = 3/2n^2 - n/2 -> 3/2n^2 - n/2 - PenNum = 0
# n=(-b±√(b²-4ac))/(2a)

def isPentagonalNumber(number):
    '''
    Checks if the number is Pentagonal (see math below)
    P = n(3n - 1)/2
    2P = 3n^2 - n
    0 = 3n^2 - n - 2P
    n = [-b ± sqrt(b^2 - 4ac)] / 2a
    n = [1 ± sqrt(1 + 24P)] / 6
    '''
    n = (((24*number + 1)**0.5)+1)/6
    return (n == int(n))


def findPentagonal(n):
    return int(n*(3*n - 1)/2)


def generatePentagonalNumbers():
    pass


if __name__ == '__main__':
    print(isPentagonalNumber(22))
    pass
