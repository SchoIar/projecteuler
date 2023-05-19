# Anton Ilic, May 17, 2023
# https://projecteuler.net/problem=51

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def replaceDigits(number):
    primesSet = set()
    numberStr = str(number)
    #iterate through all possible changes in number
    

    #iterate through all possible replacement digits
    for replacementDigit in range(0, 10):
        for digit in range(0, len(numberStr)):
            #for 1 digit..
            currentNum = list(numberStr)
            currentNum[digit] = replacementDigit
            currentString = ''
            for element in currentNum:
                currentString += str(element)
            print(currentString)
        

    if len(primesSet) == 8:
        return min(primesSet)

    
    

def getReplacedDigitPermutations(number):
    smallestPrime = None
    #part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
    
    return smallestPrime

def main():
    start = 3
    while True:
        start += 2
        if isPrime(start):
            potentialSolution = getReplacedDigitPermutations(start)
            if potentialSolution != None:
                return potentialSolution

if __name__ == '__main__':
    print(replaceDigits(123456))
    '''solution = main()
    print(solution)'''
