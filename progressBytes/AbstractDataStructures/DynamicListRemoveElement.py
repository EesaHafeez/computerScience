#Challenge: 
#Write a function that takes a list and an element as input 
#and removes the first occurrence of the element from the list.

def removeElement(list):
    element = input('Enter element: ') #inputting element
    for i in range (0,len(list)-1):
        if list[i] == element:
            list.pop(i) #removing element at that index
            return list

fruits = ['apples', 'bananas', 'oranges', 'pears', 'grapes', 'apples'] #testing code using list called fruits
print(removeElement(fruits))