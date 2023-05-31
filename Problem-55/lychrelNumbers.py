# Anton Ilic, May 30, 2023
# https://projecteuler.net/problem=55

def isPalindrome(number):
    numStr = str(number)
    return numStr == numStr[::-1]


def isLychrel(number):
    for i in range(1, 51):
        number = number + int((str(number)[::-1]))
        if isPalindrome(number):
            return False

    return True


def solution():
    isLychrelCount = 0
    for i in range(1, 10000):
        if isLychrel(i):
            isLychrelCount += 1
    return isLychrelCount


if __name__ == '__main__':
    print(solution())
