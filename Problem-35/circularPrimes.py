# Anton Ilic, Apr 26, 2023
# https://projecteuler.net/problem=35

def findLenOfListOfCircularPrimes(listOfPrimes):
    circularPrimesList = []
    for prime in listOfPrimes:
        notCircularPrime = False
        primeStr = str(prime)
        for i in range(len(primeStr)):
            shifted = primeStr[i:] + primeStr[:i] #Rotating digit by slicing
            if not isPrime(int(shifted)):
                notCircularPrime = True
                break
        if not notCircularPrime:
            circularPrimesList.append(prime)

    return len(circularPrimesList)


def possibleCircularPrimesOver100(number):
    #circular primes over 100 will only contain '1' '3' '7' and '9', and are rotations
    number = str(number)
    if ('2' in number or '4' in number or '5' in number or '6' in number or '8' in number or '0' in number):
        return False
    return True

def isPrime(number):
    if number % 2 == 0:#or possibleCircularPrimesOver100(number) == False:
        return False
    if number > 100:
        if possibleCircularPrimesOver100(number) == False:
            return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def solution():
    listOfPrimes = []
    for i in range(1, 1000001):
        if isPrime(i):
            print(i)
            listOfPrimes.append(i)
    return findLenOfListOfCircularPrimes((listOfPrimes))

# Entry point of the script
if __name__ == '__main__':
    circularPrimesCount = solution()
    print(circularPrimesCount)
