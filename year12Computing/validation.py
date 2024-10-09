database= [['eesahafeez', '1234', 'qwerty'], 
           ['qwertyuiop', '4321','asdfg' ]]

def database_search(id):
    found = False
    for i in range(len(database)):
        if database[i][0] == id:
            found=True
            list = i
    if not found:
        found = False
    return found

def character_id():
    correct_id = False
    id_check=0
    while id_check != 3 and correct_id == False :
        id = input('Enter a valid character id of 10 characters: ')
        id_check = id_check +1
        correct_id = database_search(id)
    if id_check==3:
        print('Not found in database')

character_id()

def pin_validate():
            
        pin_check=0
        if pin_check == 0:
            pin = input('Enter a 4 digit id: ') 
            if not pin.isnumeric() or len(pin) !=4:   
                pin_check = pin_check +1
                correct_pin = False
        if correct_pin == True:
            corect_pin = False
            if database[list][1] == pin:
                correct_pin == True
                print('correct')
            else:
                print('wrong pin')






