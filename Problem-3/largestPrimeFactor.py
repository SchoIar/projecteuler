#Anton Ilic, Feb 25, 2023
#https://projecteuler.net/problem=3
#Find the largest prime factor of 600851475143 

def isPrime(number):
    for i in range(2, number):
        if(number%i == 0):
            return False
    return True

#Taking from the top (ie. Largest, if taking from the bottom, would put into a list, and append most large factor)
def largestPrimeFactorFinder(number):
    largestPrimeFactor = number - 1

    while(largestPrimeFactor > 0):
        if(number%largestPrimeFactor == 0):
            if(isPrime(largestPrimeFactor)):
                return largestPrimeFactor
        else:
            largestPrimeFactor -= 1

number = 600851475143 
print(largestPrimeFactorFinder(number))