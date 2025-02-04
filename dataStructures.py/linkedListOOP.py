class Node(): # creating a new node
    # variables data, next
    def __init__(self, theData):
        self.data = theData
        self.next = None
    def changeNext(self,newNext):
        self.next = newNext

class linkedList(): # creating a new linked list
    # variables head
    def __init__(self):
        self.head = None
    def addToFront(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.changeNext(self.head)
            self.head = new_node

myList = linkedList()
myList. addToFront(222)
myList. addToFront(111)
myList. addToFront(222)

print(myList.head.data)
print(myList.head.next.data)
print(myList.head.next.next.data)




