# Anton Ilic, Apr 25, 2023
# https://projecteuler.net/problem=35

def isPrime(number):
    if number % 2 == 0:
        return False
    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            return False
    return True

## Safe assumption that any number with an even number or 0, 5 in it is not a circular prime, except 2 & 5...
## The other numbers greater then 100 SHOULD be combinations of '1' '3' '7' and '9'