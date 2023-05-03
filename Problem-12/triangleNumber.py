# Anton Ilic, updated and improved on Mar 21, 2023
# https://projecteuler.net/problem=12

def numberOfDivisors(number):
    numOfDivisors = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            if number // i == i: #perfect square
                numOfDivisors += 1
            else:
                numOfDivisors += 2 #counting both divisors
    return numOfDivisors

def findTriangleNumber():
    triangle_number = 0
    i = 1
    while True:
        triangle_number += i
        if numberOfDivisors(triangle_number) >= 500:
            return triangle_number
        i += 1

print(findTriangleNumber())
