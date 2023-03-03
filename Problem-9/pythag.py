#Anton Ilic, Feb 28, 2023
#https://projecteuler.net/problem=9
#a^2 + b^2 = c^2 AND a + b + c = 1000

#Very slow solution for Problem 9. Could be done with two loops, by calculating the 3rd variable. (using a+b+c = 1000)
#Will try to optimize later. 
                
for a in range(1,1001):
    for b in range(1, 1001):
        if((a + b + ((a**2+b**2)**0.5)) == 1000):
            print(f"Product of a, b and c " + str(a*b*int((a**2+b**2)**0.5)))
            
