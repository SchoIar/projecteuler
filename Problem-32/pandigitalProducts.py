# Anton Ilic, Apr 23, 2023
# https://projecteuler.net/problem=31

# This function checks if the product of a and b (which is c) is a pandigital number
def isPandigitalProductOf10(a, b, c):
    # Combine the digits of a, b, and c into a single string
    combined = str(a) + str(b) + str(c)

    # Check if the combined string has exactly 9 digits and if the product of a and b is c
    if len(combined) == 9 and a * b == c:
        # Iterate through the numbers 1 to 9
        for i in range(1, 10):
            # Check if the current number (as a string) is not in the combined string
            if str(i) not in combined:
                return False  # If not, it's not pandigital and we return False
        return True  # If all numbers are present, it's pandigital and we return True
    else:
        return False  # If the combined string doesn't have 9 digits or the product is incorrect, return False

# This function finds the sum of all pandigital products


def findPandigitalProductSum():
    # Create an empty list to store the pandigital products
    listOfPandigitalProducts = []

    # Iterate through all possible values of a and b
    for a in range(1, 100):
        for b in range(1, 10000): #Max limits for a, b are chosen as such since, total digits must be 9. 
            # Calculate the product of a and b
            c = a * b
            # Check if the product is pandigital and not already in the list
            if isPandigitalProductOf10(a, b, c) and c not in listOfPandigitalProducts:
                # Add the pandigital product to the list
                listOfPandigitalProducts.append(c)

    # Return the sum of all pandigital products found
    return sum(listOfPandigitalProducts)


# Entry point of the script
if __name__ == '__main__':
    # Call the function to find the sum of pandigital products and print the result
    print(findPandigitalProductSum())
