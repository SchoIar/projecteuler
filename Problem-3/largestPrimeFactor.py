#Anton Ilic, Feb 25, 2023
#https://projecteuler.net/problem=3
#Find the largest prime factor of 600851475143
#very inneficiant and slow, but will eventually give the right answer 

def isPrime(number):
    if number < 2: #-ive, 0, 1 return false.
        return False 
    for i in range(2, number // 2 + 1):
        if(number%i == 0):
            return False
    return True

#Taking from the bottom
def largestPrimeFactorFinder(number):
    largestPrimeFactor = 1
    for x in range(2, number // 2 + 1):
        if(number%x == 0):
            if(isPrime(x)):
                largestPrimeFactor = x
        x += 1
    return largestPrimeFactor

number = 600851475143 
print(largestPrimeFactorFinder(number))