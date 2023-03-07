# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=16

#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?

#slow method
num = 2**1000
num = str(num)
sumOfDigits = 0
for digit in num:
    sumOfDigits += int(digit)

print(sumOfDigits)