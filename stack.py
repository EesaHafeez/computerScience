myString = input('Please enter a word or phrase to be tested: ')
list1 = list(myString) #splitting string into a list of characters
numChars = len(list1) # getting length of list of characters

listStack = [] # creating a list to use as a stack
for i in range (0, numChars):
    listStack.append(list1[i]) # appending characters to list

wordsSame=0
for i in range (0,numChars):
    if list1[i] == listStack.pop():
        wordsSame +=1 # incrementing wordSame if item popped of stack is equal to index of string
 
if wordsSame == numChars: # if wordSame is equal to length of string, palindrome
    print('Palindrome')
else:
    print('Not palindrome')