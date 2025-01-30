busQueue = [None,None,None,None,None]
front = 0
rear = -1
size = 0
maxSize = 5
def menu():
   print('')
   print('MENU: ')
   print('1 - Add an item to the queue')
   print('2 - Remove an item from the queue')
   print('3 - Quit')

def enQueue(item):
   global rear, size
   if isFull():
      print('Sorry queue is full')
      return
   else:
      rear = (rear + 1)%5
      busQueue[rear] = item
      size = size + 1
   displayInfo()

def deQueue():
   global front, size
   if isEmpty():
      print('Sorry queue is empty')
      return
   else:
      cuurentFront = busQueue[front]
      size = size -1
      front = (front + 1)%5
      displayInfo()
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

def displayInfo():
   print(busQueue)
   print('Front: ' + str(busQueue[front]))
   print('Rear: ' + str(busQueue[rear]))
   print('')


running = True
while running == True:
   menu()
   choice = int(input('Enter choice: '))
   if choice == 1:
      data = input('Enter item you would like to add into the queue: ' )
      enQueue(data)
   elif choice == 2:
      deQueue()
   elif choice == 3:
      running = False
   else:
      print('Invalid option')



