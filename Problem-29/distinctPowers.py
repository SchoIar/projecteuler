# Anton Ilic, Apr 21, 2023
# https://projecteuler.net/problem=29

def findNumberOfDistinctPowers(aMin, bMin, aMax, bMax):
    '''Returns the number of distinct powers, for a**b, for aMin <= a <= aMax, bMin <= b <= bMax'''
    listOfNumbers = []
    for a in range(aMin, aMax + 1):
        for b in range(bMin, bMax + 1):
            if a ** b not in listOfNumbers:
                listOfNumbers.append(a ** b)
    return len(listOfNumbers)#len(listOfNumbers)

print(findNumberOfDistinctPowers(2, 2, 100, 100))