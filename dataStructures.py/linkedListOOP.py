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
        while data < current.getData():
            current = current.getPointer()
        current = Node(data,current.getPointer())
        
        


    
        





