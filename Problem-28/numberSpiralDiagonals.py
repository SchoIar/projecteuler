# Anton Ilic, Apr 18, 2023. Revised May 2nd, 2023
# https://projecteuler.net/problem=28

# Using the mathematical patern, rather then generation of spiral
def calculateSum(maxNumber):
    '''Calculates sum of diagonals of 1001 x 1001 matrix using the paterns as follows:
    Sum of NE diagonal: differences of 8, 16... 
    Sum of NW diagonal: differences of 4, 12, 20...
    Sum of SE diagonal: differences of 6, 14, 22...
    Sum of SW diagonal: differences of 2, 10, 18...
    Can conclude that there are difference of 8 per 'layer', each with a different starting value
    '''
    sum = 1
    previousNumber = 1
    increment = 2
    # Since center is '1', the initial sum is '1', the previous number is also '1' and the incriment (ie. between the spiral 1 and 3 is '2')

    while previousNumber < maxNumber ** 2:  # while smaller then the max number in the spiral
        for diagonal in range(0, 4):
            previousNumber += increment
            sum += previousNumber
        increment += 2 #each 'layer' adds two more seperation from diagonals

    return sum


if __name__ == '__main__':
    print(calculateSum(3))
