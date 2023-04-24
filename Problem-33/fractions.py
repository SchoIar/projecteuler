# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=33

def isNonTrivialFractions(a, b, c, d):
    if d == 0: #cannot divide by 0, thus making 
        pass
    elif b == c: #cancelling b & c
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

                    if c == d == 0 or a == b == 0:
                        continue
                    if a > c or (a == c and b >= d):
                        continue

                    if isNonTrivialFractions(a, b, c, d):
                        fractionsList.append(f'{a}{b}/{c}{d}')

    return fractionsList

def findSolution():
    fractions = findNonTrivialFractions()
    productOfFractions = 1
    for fraction in fractions:
        productOfFractions = productOfFractions * int(fraction[0:2]) / int(fraction[3:5])
    #denominator is the conjugate
    return (1/productOfFractions)

if __name__ == '__main__':
    print(findSolution())
