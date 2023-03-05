#Anton Ilic, Feb 27, 2023
#https://projecteuler.net/problem=5

#Calculating primes under 20 inclusive

#Using those primes to find a number which is evenly divisible for all these numbers
smallestEvenlyDivisible = 2 #by math: Could use 11, 13, 14, 16, 17, 18, 19, 20 for faster result, since numbers excluded are factors of listed numbers/must be true if listed are
    
def isEvenlyDiv(num):
    for a in range(1,21):
        if(num%a != 0):
            return False
    return True
while(isEvenlyDiv(smallestEvenlyDivisible) is False):
    smallestEvenlyDivisible += 2
    print(smallestEvenlyDivisible)
