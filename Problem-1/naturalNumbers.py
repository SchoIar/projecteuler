#Anton Ilic, Feb 25, 2023

totalSum = 0
for i in range(1,1000):
    if(i%3 == 0 or i%5 == 0):
        totalSum += i

print(str(totalSum) + " is the sum of multiples of 3 and 5 up to 1000.")
