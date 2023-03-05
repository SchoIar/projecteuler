#Anton Ilic, Feb 25, 2023
#https://projecteuler.net/problem=3
#Find the largest prime factor of 600851475143
#very inneficiant and slow, but will eventually give the right answer 

def isPrime(number):
    for i in range(2, number):
        if(number%i == 0):
            return False
    return True

#Taking from the bottom
def largestPrimeFactorFinder(number):
    largestPrimeFactor = 1
    x = 1
    for x in range(0, number-1):
        x += 1
        if(number%x == 0):
            if(isPrime(x)):
                largestPrimeFactor = x
                print(largestPrimeFactor)
    if(largestPrimeFactor == 1 and number != 1): 
        return None
    return largestPrimeFactor

number = 600851475143 
#largestPrimeFactor = largestPrimeFactorFinder(number)
print(largestPrimeFactorFinder(number))