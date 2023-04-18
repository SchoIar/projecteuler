# Anton Ilic, Apr 16, 2023
# https://projecteuler.net/problem=27

def isPrime(number):
    if number < 2: #-ive, 0, 1 return false.
        return False
    
    for i in range(2, number // 2 + 1):
        if(number%i == 0):
            return False
    return True

def findNumberOfPrimes(a, b):
    i = 0
    while isPrime(i**2 + a * i + b): #note that, by definition, since we are starting at 0, b must be prime
        i += 1
    return i

def solution():
    maxPrimesUpTo = 0; alpha = 0; beta = 0

    for a in range(-999, 1000):
        for b in range(0, 1000): 
            currentPrimesUpTo = findNumberOfPrimes(a, b)
            if currentPrimesUpTo > maxPrimesUpTo:
                maxPrimesUpTo = currentPrimesUpTo
                alpha = a
                beta = b
                

    return alpha * beta

if __name__ == '__main__':
    print(solution())
# n^2 + an + b, where |a| < 1000 and |b| ≤ 1000