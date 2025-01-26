#Challenge: 
#Write a function that takes a list and an index as input and returns the element at that index. 
#If the index is out of range, return None.

def returnElement(list):
    index = int(input('Enter index: ')) # inputting index
    if index < len(list) and index > -1: # validating range
        return list[index]
    else:
        return None
    
fruits = ['apples', 'bananas', 'oranges', 'pears', 'grapes'] #testing code using list called fruits
print(returnElement(fruits))