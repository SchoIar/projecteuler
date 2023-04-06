class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self, name):
        if(self.head == None):
            self.head = Node(name)
        else:
            tempNode = self.head
            while(tempNode.next != None):
                tempNode = tempNode.next
            tempNode.next = Node(name)

class Node():
    def __init__(self, name):
        self.name = name
        self.calculatedValue = None
        self.next = None


with open("names.txt", "r+") as file:
    for line in file:
        currentLine = line.strip().replace('"','').split(',')
        

for element in currentLine:
    pass #insert in sorted order here