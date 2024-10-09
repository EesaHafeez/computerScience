carpark =[
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty']
]

def emptyCarPark():
    for i in range(6):
        for j in range(10):
            carpark[i][j] = 'empty'
            

def parkACar():
    registration = input('Enter your registration: ')
    gridReference = input('Enter your grid refernce by entering the row then collumn with no spaces: ')

    if carpark[gridReference[0]-1][gridReference[1]-1] == 'empty':
        [gridReference[0]-1][gridReference[1]-1] = registration
    print([gridReference[0]-1][gridReference[1]-1])
parkACar()
