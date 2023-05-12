# Anton Ilic, May 10, 2023
# https://projecteuler.net/problem=44

# PenNum = 3/2n^2 - n/2 -> 3/2n^2 - n/2 - PenNum = 0
# n=(-b±√(b²-4ac))/(2a)

def isPentagonalNumber(number):
    if number < 1:
        return False
    n = (((24*number + 1)**0.5)+1)/6
    return (n == int(n))


def findPentagonal(n):
    return int(n*(3*n - 1)/2)


def solution():
    pentagonlList = []
    number = 1
    while True:
        currentPentagonalNumber = findPentagonal(number)
        for a in pentagonlList:
            if(isPentagonalNumber(abs(a-currentPentagonalNumber)) and isPentagonalNumber(a+currentPentagonalNumber)):
                return(currentPentagonalNumber - a)
        pentagonlList.append(currentPentagonalNumber)
        number += 1

        
if __name__ == '__main__':
    print(solution())
    pass
