
id= input('Enter a character id: ')
id_check=0
while id_check != 2 and len(id) != 10:
    id_check = id_check +1
    id= input('Enter a character id of 10 charcters: ')
pin_check=0
if id_check!= 2:
    if pin_check == 0:
        pin = input('Enter a 4 digit id: ') 
        if not pin.isnumeric() and len(pin) !=4:   
            pin_check = pin_check +1
