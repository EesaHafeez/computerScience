
database= [['eesahafeez', '1234', 'qwerty'], 
           ['qwertyuiop', '4321','asdfg' ]]

correct_id = False
id= input('Enter a character id: ')
id_check=0
while id_check != 2 and len(id) != 10:
    id_check = id_check +1
    id= input('Enter a character id of 10 charcters: ')
if id_check<2:
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



