# Anton Ilic, Apr 15, 2023
# https://projecteuler.net/problem=26

#def findNumOfRepeatingDigitsHelper(reciprocal):

def findNumOfRepeatingDigits(selectedNumber):
    '''Returns the number of repeating digits '''
    reciprocal = 1/selectedNumber

    return selectedNumber

def findLargestRecurringCycle(maxNum):

    potentialLargestNum = 0; potentialLargestNumDigits = 0
    for currentNumber in range(2, maxNum + 1):
        #if the number has more digitsn then the previous potentialLargest digits, set it to potentialLargest
        currentDigits = findNumOfRepeatingDigits(currentNumber)
        if potentialLargestNumDigits < currentDigits:
            potentialLargestNum = currentNumber
            potentialLargestNumDigits = currentDigits

    return potentialLargestNum

print(findLargestRecurringCycle(10))
