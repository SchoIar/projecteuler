# Anton Ilic, Apr 15, 2023
# https://projecteuler.net/problem=26

#def findNumOfRepeatingDigitsHelper(reciprocal):

def findNumOfRepeatingDigits(selectedNumber):
    reciprocal = 1/selectedNumber

    return selectedNumber

def findLargestRecurringCycle(maxNum):
    potentialLargest = 0
    for largestRepeatingNum in range(2, maxNum + 1):
        potentialLargest = max(findNumOfRepeatingDigits(largestRepeatingNum), potentialLargest)
    return potentialLargest

print(findLargestRecurringCycle(10))
