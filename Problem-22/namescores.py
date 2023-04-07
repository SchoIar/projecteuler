# Anton Ilic, completed Apr 5, 2023
# https://projecteuler.net/problem=22
class LinkedList():
    def __init__(self):
        self.head = None  
    
    def insertInOrder(self, name):
        name = name.lower()
        if(self.head == None):
            #when empty inserting at head
            self.head = Node(name)
            return True
        elif(self.head.name > name):
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
            previousNode = None
            while(tempNode.name <= name): #iterate down until is LARGER or equal to current      
                if tempNode.next == None:
                    tempNode.next = insertedNode
                    insertedNode.previous = tempNode
                    return True 
                previousNode = tempNode      
                tempNode = tempNode.next
            if previousNode != None:
                previousNode.next = insertedNode
                insertedNode.previous = previousNode
            insertedNode.next = tempNode
            tempNode.previous = insertedNode
            return True
            
    def totalValues(self):
        totalValues = 0; number = 1
        tempNode = self.head
        while(tempNode != None):
            currentTotal = 0
            for element in tempNode.name:
                currentTotal += (ord(element)-96)
            totalValues += currentTotal * number
            tempNode = tempNode.next
            number += 1

        return totalValues
class Node():
    def __init__(self, name):
        self.name = name
        self.calculatedValue = None
        self.next = None
        self.previous = None

if __name__ == "__main__":
    namesList = LinkedList()
    
    with open("names.txt", "r+") as file:
        for line in file:
            currentLine = line.strip().replace('"','').split(',')
            
    for element in currentLine:
        namesList.insertInOrder(element)
    
    print(namesList.totalValues())

    