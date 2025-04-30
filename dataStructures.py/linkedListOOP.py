class Node:
    def __init__ (self,Data, pointer):
        self.data = Data
        self.pointer = pointer

    def setPointer(self, newPointer):
        self.pointer = newPointer

    def getPointer(self):
        return self.pointer
    
    def getData(self):
        return self.data
    
    def changedata(self, newdata):
        self.data = newdata



class linkedlist:
    def __init__(self,data):
        self.head = Node(data, None)
        self.tail = self.head
    def getTail(self):
        return self.tail
    def getHead(self):
        return self.head

    def addNode(self, data):
        current = self.head
        if current.getData() > data:
            self.head = Node(data,current)
        elif current.getData() <= data:
            while (current.getPointer() is not None) and (data >= current.getPointer().getData()):
                current = current.getPointer()
            current.setPointer(Node(data,current.getPointer()))
            if current.getPointer().getPointer() == None:
                self.tail = current.getPointer()

    def deleteNode(self,data):
        current = self.head
        if current.getData() == data:
            self.head = current.getPointer()
        elif current.getData != data:
            while current.getPointer() is not None and current.getPointer().getData() != data:
                current = current.getPointer() 
            current.setPointer(current.getPointer().getPointer())
            if current.getPointer() == None:
                self.tail = current
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getPointer()
        

# print('Menu system: ')
# print('1 - Add an item')
# print('2 - Delete an item')
# print('3 - Print list')
# choice = int(input('Enter a number: '))
# if



newList = linkedlist(1)
newList.addNode(10)
newList.addNode(3)
newList.addNode(7)
print("traversal") 
newList.traverse()
newList.deleteNode(7)
newList.deleteNode(1)
newList.deleteNode(10)
print("traversal") 
newList.traverse()
newList.addNode(2)
newList.addNode(3)
newList.addNode(5)
print("traversal") 
newList.traverse()
newList.deleteNode(3)
print("traversal") 
newList.traverse()









        
        


    
        





