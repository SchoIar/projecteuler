# Anton Ilic, May 30, 2023
# https://projecteuler.net/problem=58

def isPrime(number):
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def solution():
    sum = 1
    previousNumber = 1
    increment = 2
    numberOfPrimes = 0

    while True:  
        for diagonal in range(0, 4): #for individual spiral
            previousNumber += increment
            if isPrime(previousNumber):
                numberOfPrimes += 1
        
        #previousNumber is the last diagonal of the layer - has the 'count' of numbers
        #rint(previousNumber / numberOfPrimes)

        increment += 2  # each 'layer' adds two more seperation from diagonals

