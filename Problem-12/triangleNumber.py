# Anton Ilic, Mar 4, 2023
# https://projecteuler.net/problem=12

def calculateDivisors(number):
    #divisiorsFound = []

    numOfDivisors = 2 #removes redudant calculation for the number itself and 1. 
    for i in range(2,number):
        if(number%i == 0):
            numOfDivisors += 1
    #return len(divisiorsFound)
    return numOfDivisors

i = 0; n = 1 #i for iterated numbr, n for difference in triangle num.
while(calculateDivisors(i) < 500):
    i += n; n += 1
    
print(i)