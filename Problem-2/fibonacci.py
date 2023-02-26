#Anton Ilic, Feb 25, 2023
#https://projecteuler.net/problem=2

#Sum of even valued Fibonacci terms, up to 4 million
#Note: This method is the slow way. Can also calculate via properties of fibonaci numbers, notably that every 3rd number is even (ie. Two odd numbers make an even number)
totalSumOfModTwos = 0
previousFib = 1; nextFib = 1
i = 0

while(i < 4000000):
    if(i%2 == 0):
        totalSumOfModTwos += i
    nextFib = i
    i = previousFib + nextFib
    previousFib = nextFib

    
print(totalSumOfModTwos)