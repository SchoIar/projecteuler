# Anton Ilic, Apr 21, 2023
# https://projecteuler.net/problem=29

def solution():
    listOfNumbers = []
    for a in range(2, 101):
        for b in range(2, 101):
            if a ** b not in listOfNumbers:
                listOfNumbers.append(a ** b)
    return len(listOfNumbers)#len(listOfNumbers)

print(solution())