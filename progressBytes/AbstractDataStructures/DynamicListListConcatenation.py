#Write a function that takes two lists as input and returns a new list containing elements from both lists

def list_concatenation (list1,list2):
    for i in range (0,len(list2)):
        list1.append(list2[i]) #adding elements of list 2 onto list 1
    return list1 #returning new list

fruits = ['apples', 'pears', 'oranges']
vegetables = ['brocoli','tomatos','potatos']    

print(list_concatenation(fruits,vegetables)) #testing using 2 lists