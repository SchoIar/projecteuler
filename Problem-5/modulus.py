#Anton Ilic, Feb 27, 2023, revised April 17, 2023
#https://projecteuler.net/problem=5

## Using a new approach, considering that the LCM of 1-20 must be the selected number

import math

# Function to calculate the least common multiple (LCM) of two numbers, using GCD. 
def findLCM(a, b):
    lcm = (a * b) // math.gcd(a, b)
    return lcm

# Function to calculate the smallest number evenly divisible by all numbers in the range 1 to 20
def find_smallest_evenly_divisible():
    current_lcm = 1
    for number in range(1, 21):
        current_lcm = findLCM(current_lcm, number)
    return current_lcm

# Call the find_smallest_evenly_divisible function and print the result
print(find_smallest_evenly_divisible())