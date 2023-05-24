# Anton Ilic, May 17, 2023
# https://projecteuler.net/problem=51

from itertools import combinations

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def replace_number_indices(number, indices, replacement_digit):
    number = list(str(number))
    for index in indices:
        number[index] = str(replacement_digit)
    return int(''.join(number))

def replace_digits(number, family_size):
    str_num = str(number)
    len_num = len(str_num)
    for num_indices in range(1, len_num):
        for indices in combinations(range(len_num), num_indices):
            prime_family = set()
            for replacement_digit in range(10):
                replaced_num = replace_number_indices(number, indices, replacement_digit)
                if is_prime(replaced_num):
                    # ignore leading zeros
                    if len(str(replaced_num)) == len_num:
                        prime_family.add(replaced_num)
            if len(prime_family) == family_size:
                return min(prime_family)
    return None

def main():
    number = 11
    while True:  # starting from 11 and step of 2 to speed up search
        if is_prime(number):
            potential_solution = replace_digits(number, 8)
            if potential_solution is not None:
                return potential_solution
        number += 2
    return None

if __name__ == '__main__':
    solution = main()
    print(solution)
