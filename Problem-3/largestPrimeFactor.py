#Anton Ilic, Feb 25, 2023, revised April 17, 2023
#https://projecteuler.net/problem=3

def largestPrimeFactorFinder(number):
    i = 2
    while i ** 2< number:
        while number % i == 0:
            number = number / i #breaking down the initial number by prime factors, since product of prime factors is the number 
        i = i + 1

    return int(number)

number = 600851475143 
print(largestPrimeFactorFinder(number))