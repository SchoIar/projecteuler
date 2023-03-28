# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=15

#Representing 20 x 20 grid by it's coordinates, then performing a breadth first search

grid = []
line = []
for x in range(0, 21):
    line = []
    for y in range(0, 21):
        a = (x, y)
        line.append(a)
    grid.append(line)
        
print(grid)


#See https://en.wikipedia.org/wiki/Permutation for mathematical explanation for problem.

