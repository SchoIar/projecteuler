# Anton Ilic, Apr 27, 2023
# https://projecteuler.net/problem=37
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def isTruncablePrime(number):
    if not isPrime(number):  # single digit numbers and non-primes aren't truncatable primes
        return False
        
    strNumber = str(number)  
    for i in range(1, len(strNumber)):
        leftSlice = strNumber[i:]  # e.g., number is 378 -> 78 -> 8
        rightSlice = strNumber[:-i]  # e.g., number is 378 -> 37 -> 3
        if not (isPrime(int(rightSlice)) and isPrime(int(leftSlice))):
            return False
        
    return True

def solution():
    truncatable_primes = []
    i = 11  # single digits are not truncable
    while len(truncatable_primes) < 11:  # there are only 11 such truncatable primes
        if isTruncablePrime(i):
            truncatable_primes.append(i)
            
        i += 2  # only check odd numbers
    return sum(truncatable_primes)

if __name__ == '__main__':
    print(solution())


