class Node:
    def __init__ (self,data,pointer):
        self.data = data
        self.pointer = pointer
    def getPointer(self):
        return self.pointer
    def setPointer(self,pointer):
        self.pointer = pointer
    def getData(self):
        return self.data
    def setData(self,data):
        self.data = data



class Stack:
    def __init__(self,data):
        self.top = Node(data,None)
    
    def addItem(self,data):
        self.top = Node(data,self.top)

    def popItem(self):
        dataToReturn = self.top.getData()
        self.top = self.top.getPointer()
        return dataToReturn
        
        



    





newStack = Stack('eesa')
newStack.addItem('Husaam')
newStack.popItem()
print(newStack.top.getData())   



