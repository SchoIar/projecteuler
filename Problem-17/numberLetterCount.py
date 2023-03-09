# Anton Ilic, Mar 6, 2023
# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used? NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def singleDigit(num):
    '''Assumes input is a single digit'''
    count = 0
    if num == 0:
        return 0 #one two six
    elif (num == 1 or num == 2 or num == 6):
        count = 3 #four five nine
    elif (num == 4 or num == 5 or num == 9):
        count = 4
    else: #three  seven eight
        count = 5
    return count


def doubleDigit(num):
    numStr = str(num)
    firstNum = int(numStr[0])
    secondNum = int(numStr[1])
    count = 0
    if firstNum == 1:
        if (num == 10):
            count = 3
        elif (num == 11 or num == 12): #eleven twelve
            count = 6
        elif (num == 13 or num == 14 or num == 18 or num == 19):
            count = 8 #fourTEEN
        elif (num == 15 or num == 16): #sixteen = 7 AND
            count = 7
        elif (num == 17):  # 17 seventeen
            count = 9
        return count
        #twenty thirty eighty ninety
    elif firstNum == 2 or firstNum == 3 or firstNum == 8 or firstNum == 9:
        return 6 + singleDigit(secondNum)
    elif firstNum == 7: #seventy
        return 7 + singleDigit(secondNum)
    else: #forty fifty sixty 
        return 5 + singleDigit(secondNum)



def tripleDigit(num):
    numStr = str(num)
    firstNum = int(numStr[0])
    secondNum = int(numStr[1])
    thirdNum = int(numStr[2])
    firstAndSecondNum = int(str(secondNum) + str(thirdNum))

    count = singleDigit(firstNum) + 7

    if(secondNum == 0 and thirdNum == 0): #case: X hundred
        return count
    elif(secondNum == 0):
        return count + singleDigit(thirdNum) + 3 #case: X hundred and Y
    else:
        return count + doubleDigit(firstAndSecondNum) + 3 #case: X hundred and YZ
    

totalSum = 0
for i in range(1,1001):
    if(i < 10):
        totalSum += singleDigit(i)
    elif(i < 100):
        totalSum += doubleDigit(i)
    elif(i < 1000):
        totalSum += tripleDigit(i)
        #print(f"{i} and {tripleDigit(i)}")
    else:
        totalSum += 11
    

print(totalSum)

