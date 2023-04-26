# Anton Ilic, Apr 25, 2023
# https://projecteuler.net/problem=34

# Function to calculate the factorial of a given number
def factorial(element):
    fsum = 1
    for i in range(1, element + 1):
        fsum = fsum * i  
    return fsum  

# Function to check if the sum of the factorials of the digits of a number is equal to the number itself
def is_digits_equal_to_factorial(number, factorial_dict):
    number_str = str(number) 
    factorial_sum = 0 

    for element in number_str:
        # Add the factorial of the digit to the sum of factorials
        if int(element) in factorial_dict:
            factorial_sum += factorial_dict[int(element)]
        else:
            factorial_sum += factorial(int(element))

    if(number == factorial_sum):
        return True  
    return False  

# Function to find the sum of numbers that satisfy the is_digits_equal_to_factorial condition up to a given maximum number
def solution(max_number):
    '''Finds all cases where the digits of the number as factorials are equal to the number'''
    factorial_dict = {}
    for number in range(0, 10):  # Including 0 in the range to cover the factorial of 0
        factorial_dict[number] = factorial(number)

    sum_of_digits_equal_to_factorial = 0 
    for current_number in range(3, max_number):
        if is_digits_equal_to_factorial(current_number, factorial_dict) == True:
            sum_of_digits_equal_to_factorial += current_number
    return sum_of_digits_equal_to_factorial 

# Entry point of the script
if __name__ == '__main__':
    # Since 9999999 > 9! * 7, all greater numbers will be smaller than their sum of digit factorials
    print(solution(factorial(9) * 7))  
