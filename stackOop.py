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
    def peekItem(self):
        return self.top.getData()
    def isEmpty(self):
        if self.top == None:
            return True
    def getTop(self):
        return self.top

        

        
        



    





name = input('Enter a word: ')
newStack = Stack(name[0])

for i in range (1,len(name)):
    newStack.addItem(name[i])
wordSame = 0
for i in range(0,len(name)):
    if newStack.popItem() == name[i]:
        wordSame = wordSame + 1

if wordSame == len(name):
    print('Is palindrome')
else:
    print('Not palindrome')


