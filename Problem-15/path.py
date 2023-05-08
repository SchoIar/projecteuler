# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=15

def factorial(n):
    nFactorial = 1
    for i in range(1, n + 1):
        nFactorial = nFactorial * i
    return nFactorial

def solvebyBinomialCoefficient(n, k):
    #n represents the total number of moves (40 in this case), and k represents the number of right moves (20 in this case)
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

print(solvebyBinomialCoefficient(40, 20))