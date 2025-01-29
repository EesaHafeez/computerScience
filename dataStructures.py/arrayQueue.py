busQueue = [None,None,None,None,None]
front = 0
rear = -1
size = 0
maxSize = 5

def enQueue(item):
   global rear, size
   if isFull():
      print('Sorry queue is full')
      return
   else:
      rear = rear + 1
      busQueue[rear] = item
      size = size + 1

def deQueue():
   global front, size
   if isEmpty():
      print('Sorry queue is empty')
      return
   else:
      cuurentFront = busQueue[front]
      size = size -1
      front = front + 1
      return cuurentFront
   

def isFull():
   if size == maxSize:
      return True
   else:
      return False

def isEmpty():
   if size == 0:
      return True
   else:
      return False

enQueue(21)
enQueue(76)
enQueue(141)
enQueue(243)
enQueue(149)
enQueue(271)
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())




print(busQueue)