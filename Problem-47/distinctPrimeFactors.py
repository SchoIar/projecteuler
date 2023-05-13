# Anton Ilic, May 12, 2023
# https://projecteuler.net/problem=47

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True


def findDistinctPrimeFactors(n, listOfFactors):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: #smallest number found is always the prime factor.
            if i not in listOfFactors: #for distinct prime factors, only appending 
                listOfFactors.append(i) 
            return findDistinctPrimeFactors(n/i, listOfFactors)
    listOfFactors.append(int(n))
    return listOfFactors

def solution():
    i = 4
    while True:
        for num in range(0, 5):
            arrayOfPrimeFactors = findDistinctPrimeFactors((i + num),[])
            arrayLength = len(arrayOfPrimeFactors)
            if arrayLength == 4:
                continue
            if num == 4:
                print(findDistinctPrimeFactors(i, []))
                print(findDistinctPrimeFactors(i + 1, []))
                print(findDistinctPrimeFactors(i + 2, []))
                print(findDistinctPrimeFactors(i + 3, []))
                return i
            
            break
        i += 1

if __name__ == '__main__':
    print(solution())
