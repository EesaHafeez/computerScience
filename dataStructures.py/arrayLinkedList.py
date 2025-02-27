names = ['Husaam', 'Eesa', 'Rezwan', 'Kaya', 'Altaf']

first = 4
data = 0
nextPointer = 1
nextFree = 5

linkedList = [
    ['Husaam' , 3],
    ['Eesa' , 0],
    ['Rezwan' , None],
    ['Kaya' , 2],
    ['Altaf' , 1],
    [None , None],
]


def traverse():
    current = first
    while current != None:
        print(linkedList[current][data])
        current = linkedList[current][nextPointer]

traverse()
