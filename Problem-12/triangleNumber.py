# Anton Ilic, updated and improved on Mar 21, 2023
# https://projecteuler.net/problem=12

# Let prime factorization of n = p1^a1 * p2^a2.... *pn^an 
# total num of divisors is (a1+1)(a2+1)...(an+1)


def numberOfDivisors(number):
    #divisiorsFound = []

    numOfDivisors = 2 #removes redudant calculation for the number itself and 1. 
    for i in range(2,number): #could take the sqrt to solve. 
        if(number%i == 0):
            numOfDivisors += 1
    #return len(divisiorsFound)
    return numOfDivisors

i = 0; n = 1 #i for iterated numbr, n for difference in triangle num.
while(numberOfDivisors(i) < 500):
    i += n; n += 1
    
print(i)