# Anton Ilic, Apr 15, 2023
# https://projecteuler.net/problem=26
#

def findNumOfRepeatingDigits(selectedNumber):
    '''Returns the number of repeating digits '''
    reciprocal = 1/selectedNumber
    reciprocal = str(reciprocal) 
    reciprocal = reciprocal[2::] #removing '0.' characters
    for i in range(0, len(reciprocal)):
        reciprocalSlice = reciprocal[i::]
        if reciprocalSlice * (len(reciprocal) // len(reciprocalSlice)) in reciprocal:
            #Checking if the repeating slice (substring) can be repeated n times and in contents of the original string, the reason for ignoring remainder is that, the non repeated characters have to be ignored
            return len(reciprocalSlice)
        
    return 0

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
