# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=33

# This function checks if the fractions a/b and c/d are equal when b and c are canceled out
def isNonTrivialFractions(a, b, c, d):
    if d == 0:  # Cannot divide by 0, thus making the fraction invalid
        return False
    elif b == c:  # Canceling b & c
        numerator = str(a) + str(b)
        denominator = str(c) + str(d)
        fraction = int(numerator) / int(denominator)
        if a / d == fraction:
            return True
    return False

# This function finds all non-trivial fractions with the described conditions
def findNonTrivialFractions():
    fractionsList = []

    # Fractions in the form 'ab/cd', where ab != 0 and cd != 0
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):

                    if c == d == 0 or a == b == 0:
                        continue
                    if a > c or (a == c and b >= d):
                        continue

                    if isNonTrivialFractions(a, b, c, d): #append fractions as tuples; (numerator, denominator)
                        fractionsList.append((int(f'{a}{b}'), int(f'{c}{d}')))

    return fractionsList

# This function calculates the product of all the non-trivial fractions found
def findSolution():
    fractions = findNonTrivialFractions()
    productOfFractions = 1
    for numerator, denominator in fractions:
        productOfFractions = productOfFractions * numerator / denominator
    # The denominator of the simplified product is the conjugate of the reciprocal
    return (1 / productOfFractions)

# Entry point of the script
if __name__ == '__main__':
    print(findSolution())
