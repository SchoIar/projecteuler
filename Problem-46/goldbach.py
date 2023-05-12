# Anton Ilic, May 11, 2023
# https://projecteuler.net/problem=46

#Odd composite numbers (all the odd integers that are not prime).

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    #must be an ODD prime + a 2 ** alpha
    primesList = []
    start = 9
    for i in range(2, start):
        if isPrime(i):
            primesList.append(i)
    while True:
        if isPrime(start):
            primesList.append(start)
        else:
            #test if composite = prime + 2 * a^2
            # => a = root((comp-prime)/2)
            pass
        
        start += 2