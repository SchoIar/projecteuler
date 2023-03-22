# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=18

#Potential to use a BST
"""class Node:
    def __init__(self, data, parent, left, right):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self, head):
        self.head = None
    
    def 
"""


numbers = []
with open('data.txt') as f:
    for line in f:
        numToInsert = []
        for field in line.split():
            numToInsert.append(int(field))
        numbers.append(numToInsert)
