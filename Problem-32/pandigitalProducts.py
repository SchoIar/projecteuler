# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=31

# This function checks if the product of a and b (which is c) is a pandigital number
def isPandigitalProductOf10(a, b, c):
    combined = str(a) + str(b) + str(c)
    # Check if the combined string has exactly 9 digits and if the product of a and b is c
    if len(combined) == 9 and a * b == c:
        for i in range(1, 10):
            # Check if the current number (as a string) is not in the combined string
            if str(i) not in combined:
                return False  # If not, it's not pandigital and we return False
        return True  # If all numbers are present, it's pandigital and we return True
    else:
        return False  # If the combined string doesn't have 9 digits or the product is incorrect, return False


def findPandigitalProductSum():

    listOfPandigitalProducts = []

    for a in range(1, 100):
        # Max limits for a, b are chosen as such since, total digits must be 9.
        for b in range(1, 10000):
            c = a * b
            # Check if the product is pandigital and not already in the list
            if isPandigitalProductOf10(a, b, c) and c not in listOfPandigitalProducts:
                listOfPandigitalProducts.append(c)

    return sum(listOfPandigitalProducts)


if __name__ == '__main__':
    print(findPandigitalProductSum())
