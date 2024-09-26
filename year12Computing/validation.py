database= [['eesahafeez', '1234', 'qwerty'], 
           ['qwertyuiop', '4321','asdfg' ]]

def database_search():
    found = False
    for i in range(len(database)):
        if database[i][0] == id:
            found=True
    if not found:
        found = False
    return found


correct_id = False
id= input('Enter a character id: ')
correct_id = database_search()
id_check=0
while id_check != 2 and correct_id == False :
    id_check = id_check +1
    id= input('Enter a valid character id of 10 characters: ')
    correct_id = database_search()
if id_check==2:
    print('Not found in database')
if id_check<3:
    for i in range(len(database)):
        if database[i][0] == id:
            correct_id = True
            list = i

correct_pin = True
if correct_id == True:
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






