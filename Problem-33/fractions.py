# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=33

def isNonTrivialFractions(a, b, c, d):
    if b == 0 or d == 0:
        pass
    elif b == c:
        numerator = str(a) + str(b)
        denominator = str(c) + str(d)
        fraction = int(numerator) / int(denominator)
        if a / d == fraction:
            return True
    return False

def findNonTrivialFractions():
    fractionsList = []

    #Fractions in form 'ab/cd', where ab != 0 and cd != 0
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):

                    #ignoring 0, or cases where denominator is 0 (DNE)
                    if c == d == 0 or a == b == 0:
                        continue

                    if a > c or (a == c and b >= d):
                        continue

                    if isNonTrivialFractions(a, b, c, d):
                        fractionsList.append(f'{a}{b}/{c}{d}')

    return fractionsList

if __name__ == '__main__':
    print(findNonTrivialFractions())