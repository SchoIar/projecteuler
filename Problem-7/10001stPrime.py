#Anton Ilic, Feb 28, 2023
#https://projecteuler.net/problem=7
#10 001st prime number

#prime numbers cannot be multiples of 2 (can incriment by 2.)
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13..


primeList = [2]
currentNumber = 3

while(len(primeList) < 10001):
    isPrime = True
    for primeNumber in primeList:
        if(currentNumber%primeNumber == 0): #ie: It isn't a prime
            isPrime = False
            break
    if(isPrime == True):
        primeList.append(currentNumber)
        print(currentNumber)
    currentNumber = currentNumber + 2
    

