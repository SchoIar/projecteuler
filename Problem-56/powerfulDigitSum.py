# Anton Ilic, May 30, 2023
# https://projecteuler.net/problem=56


def sumOfDigits(number):
    numStr = str(number)
    sumOfDigits = 0
    for digit in numStr:
        sumOfDigits += int(digit)
    return sumOfDigits

def solution(maxNumber):
    maxSum = 0
    for a in range(1, maxNumber + 1):
        for b in range(1, maxNumber + 1):
            currentSum = sumOfDigits(a ** b)    
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum

if __name__ == '__main__':
    print(solution(100))
