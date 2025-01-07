# creating a list
list_names = ['Eesa','Husaam','Kaya','Rezwan']
def element_output(list):
    
    index = int(input('Enter index number: '))
    if index in range (len(list)):
        return list[index]
    else:
        return None
print(element_output(list_names))
