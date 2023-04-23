# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=31

# sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def isPandigitalProductOf10(a, b, c):
    combined = str(a) + str(b) + str(c)
    if len(combined) == 9 and a * b == c:
       for i in range(1, 10):
            if str(i) not in combined:
                return False
       return True
    else:
        return False


def findPandigitalProductSum(min, max):
    pass

if __name__ == '__main__':
    print(isPandigitalProductOf10(39, 186, 7254))
#   solution = findPandigitalProductSum(1, 9)
#   print(solution)
