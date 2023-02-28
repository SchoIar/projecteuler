#Anton Ilic, Feb 27, 2023
#https://projecteuler.net/problem=5
def isDivisible(number):
    for i in range(1,21):#from 1 to 20
        if(number%i != 0):
            return False
    return True

i = 2
while(isDivisible(i) != True):
    i += 2
print(i)