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
    complete = False
    while complete == False:
        correctRange=False
        while correctRange == False:
            if (int(gridReference[0])-1) > -1 and (int(gridReference[0])-1) < 6:
                if (int(gridReference[1])-1) > -1 and (int(gridReference[1])-1) < 10:
                    correctRange = True
            else:
                gridReference = input('Enter a correct range. Rows range from 1-6 and collumns from 1-10: ')

        if carpark[int(gridReference[0])-1][int(gridReference[1])-1] == 'empty' and correctRange == True:   
                carpark[int(gridReference[0])-1][int(gridReference[1])-1] = registration
                complete = True
    print(carpark[int(gridReference[0])-1][int(gridReference[1])-1])

parkACar()

parkACar()