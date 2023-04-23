# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=31

def isPandigitalProductOf10(a, b, c):
    combined = str(a) + str(b) + str(c)
    if len(combined) == 9 and a * b == c:
       for i in range(1, 10):
            if str(i) not in combined:
                return False
       return True
    else:
        return False

def findPandigitalProductSum():
    listOfPandigitalProducts = []
    a = 0; b = 0; c = 0; 
    for a in range(0, 100):
        for b in range(0, 10000):
            c = a * b
            if isPandigitalProductOf10(a, b, c) and c not in listOfPandigitalProducts:
                listOfPandigitalProducts.append(c)
    return sum(listOfPandigitalProducts)

if __name__ == '__main__':
    print(findPandigitalProductSum())
