# Anton Ilic, completed Apr 5, 2023
# https://projecteuler.net/problem=22
class LinkedList():
    def __init__(self):
        self.head = None  
    
    def insertInOrder(self, name):
        if(self.head == None):
            self.head = Node(name)
            return True
        elif(self.head.name < name):
            #inserting at head when head node exists. 
            newNode = Node(name)
            headNode = self.head
            headNode.previous = newNode
            newNode.next = headNode
            self.head = newNode
            return True
        else:
            insertedNode = Node(name)
            tempNode = self.head
            while(tempNode.name >= name): #iterate down untill is LARGER or equal to current      
                if tempNode.next == None:
                    tempNode.next = insertedNode
                    insertedNode.previous = tempNode
                    return True 
                previousNode = tempNode      
                tempNode = tempNode.next
            previousNode.next = insertedNode
            insertedNode.previous = previousNode
            insertedNode.next = tempNode
            tempNode.previous = insertedNode
            return True
            
    def printList(self):
        tempNode = self.head
        while(tempNode != None):
            print(f"{tempNode.name}")
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
    namesList.insertInOrder(111)
    namesList.insertInOrder(9)
    namesList.insertInOrder(91)
    namesList.printList()
    #namesList.printList()
    