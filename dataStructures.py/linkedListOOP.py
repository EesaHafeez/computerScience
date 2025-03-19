class Node :
    def __init__ (self, myData):
        self.data = myData
        self.pointer = None

    def changePointer(self, newPointer):
        self.pointer = newPointer

    def getPointer(self):
        return self.pointer
    
    def getdData(self):
        return self.data
    
    def changedata(self, newdata):
        self.data = newdata



class linkedlist:
    def __init__(self,data):
        newNode = Node(data)
        self.head = newNode.getPointer()
        self.Tail = newNode.getPointer()

    def addNode(self, data):
        self.new_node = Node(data)
    
        





