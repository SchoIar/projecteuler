# Anton Ilic, completed Apr 5, 2023
# https://projecteuler.net/problem=22
class LinkedList():
    def __init__(self):
        self.head = None  
    
    def insertInOrder(self, name):
        if(self.head == None):
            self.head = Node(name)
        elif(self.head.name < name):
            #inserting at head when head node exists. 
            newNode = Node(self.head.name)
            self.head.next = newNode
            self.head.name = name
            
    """ else:
        tempNode = self.head
        while(tempNode.name >= name):             
            tempNode = tempNode.next

        nextNode = tempNode.next
        insertedNode = Node(name)
        insertedNode.next = nextNode
        tempNode.next = nextNode"""
            
                
    def printList(self):
        tempNode = self.head
        while(tempNode != None):
            print(f"{tempNode.name}, \n")
            tempNode = tempNode.next

class Node():
    def __init__(self, name):
        self.name = name
        self.calculatedValue = None
        self.next = None
        self.previous = None

        

"""
with open("names.txt", "r+") as file:
    for line in file:
        currentLine = line.strip().replace('"','').split(',')
        

for element in currentLine:
    pass #insert in sorted order here
"""
if __name__ == "__main__":
    namesList = LinkedList()
    namesList.insertInOrder(10)
    namesList.insertInOrder(11)
    namesList.insertInOrder(99)
    namesList.insertInOrder(11)
    namesList.printList()
    #namesList.printList()
    