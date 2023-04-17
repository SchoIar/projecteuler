# Anton Ilic, Apr 16, 2023
# https://projecteuler.net/problem=26

def findNumOfRepeatingDigits(selectedNumber):
    '''Returns the number of repeating digits '''
    remainder = 1; remainderList = [] #starting at 1, since we take the remainder of the numerator (ie. 1/n, remainder is 1)
    while remainder not in remainderList: #essentially performing long division by hand till reach 0.
        remainderList.append(remainder)
        remainder = (remainder * 10) % selectedNumber #shifting decimal right
    return len(remainderList)

        

def findLargestRecurringCycle(maxNum):
    '''Finds largest recurring cycle for reciprocal of 1/2 to 1/n'''
    potentialLargestNum = 0; potentialLargestNumDigits = 0
    for currentNumber in range(2, maxNum + 1):
        #if the number has more digitsn then the previous potentialLargest digits, set it to potentialLargest
        currentDigits = findNumOfRepeatingDigits(currentNumber)
        if potentialLargestNumDigits < currentDigits:
            potentialLargestNum = currentNumber
            potentialLargestNumDigits = currentDigits
    return potentialLargestNum

if __name__ == '__main__':
    print(findLargestRecurringCycle(1000))
