# Anton Ilic, Mar 5, 2023
#https://projecteuler.net/problem=13

#Note: I solved this problem using XLS, then came back to it in python.
numbers = []
with open('numbers.txt') as f:
    for line in f:
        numbers.append(int(line.strip()))

solution = sum(numbers)
solution = str(solution)[0:10] 
f.close()
print(solution)