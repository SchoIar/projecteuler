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
        pass
    elif (num == 1 or num == 2 or num == 6):
        count = 3
    elif (num == 4 or num == 5 or num == 9):
        count = 4
    else:
        count = 5
    return count


def doubleDigit(num):
    if(num == 0):
        return 0
    numStr = str(num)
    firstNum = int(numStr[0])
    secondNum = int(numStr[1])

    if firstNum == 1:
        if (num == 10):
            return 3
        elif (num == 11):
            return 5
        elif (num == 12):
            return 6
        elif (num == 13 or num == 14 or num == 18 or num == 19):
            return 8
        elif (num == 15):
            return 7
        else:  # 17
            return 9
    elif firstNum == 2 or firstNum == 3 or firstNum == 8 or firstNum == 9:
        return 6 + singleDigit(secondNum)
    elif num == 70:
        return 7 + singleDigit(secondNum)
    else:
        return 5 + singleDigit(secondNum)

        #eleven twelve thirteen fourteen fifteen sixteen seventeen
        # eighteen nineteen twenty. thirty
        # forty fifty sixty seventy eighty ninety


def tripleDigit(num):
    numStr = str(num)
    count = singleDigit(int(numStr[0])) + 7

    if(int(numStr[1]) == 0):
        count += 3 + singleDigit(int(numStr[2]))
    else:
        count += doubleDigit(int(numStr))

    return count

totalSum = 0
for i in range(1,1001):
    if(i < 10):
        totalSum += singleDigit(i)
    elif(i < 100):
        totalSum += doubleDigit(i)
    elif(i < 1000):
        totalSum += tripleDigit(i)
    else:
        totalSum += 11

print(totalSum)
print(tripleDigit(300))
print(tripleDigit(342))