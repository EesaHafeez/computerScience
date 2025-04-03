class Node :
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
            while current.getPointer() is not None and data >= current.getPointer().getData():
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




newList = linkedlist(5)
newList.addNode(6)
newList.addNode(5454)
newList.addNode(0)


print('Head = ' + str(newList.getHead().getData()))
print('Tail = ' + str(newList.getTail().getData()))
print('')
print(newList.getHead().getData())
print(newList.getHead().getPointer().getData())
print(newList.getHead().getPointer().getPointer().getData())
print(newList.getHead().getPointer().getPointer().getPointer().getData())

newList.deleteNode(5454)

print('Head = ' + str(newList.getHead().getData()))
print('Tail = ' + str(newList.getTail().getData()))
print('')
print(newList.getHead().getData())
print(newList.getHead().getPointer().getData())
print(newList.getHead().getPointer().getPointer().getData())




        
        


    
        





