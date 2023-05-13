# Anton Ilic, May 13, 2023
# https://projecteuler.net/problem=48

def findLastTenDigits(n):
    return str(n ** n)[-10:]


def findLastTenDigitsSum(n):
    lastTenDigits = 0
    for currentNumber in range(1, n + 1):
        lastTenDigits += int(findLastTenDigits(currentNumber))
    return str(lastTenDigits)[-10:]


if __name__ == '__main__':
    solution = findLastTenDigitsSum(1000)
    print(solution)
