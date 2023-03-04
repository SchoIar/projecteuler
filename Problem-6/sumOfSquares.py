#Anton Ilic, Feb 27, 2023
#https://projecteuler.net/problem=6
#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.
sumOfSquares = 0
squareOfSum = 0
for i in range(0,101):
    sumOfSquares += i*i
    squareOfSum += i

squareOfSum = squareOfSum * squareOfSum
print(abs(sumOfSquares - squareOfSum))