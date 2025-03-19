arrayNum=[None, None, None, None, None, None, None, None, None, None]
top = -1

def isFull():
    global top
    if top == 9:
        return True

def isEmpty():
    global top
    if top == -1:
        return True
    
def pushItem(item):
    global top
    arrayNum[top+1] = item
    top  = top + 1

def popItem():
    global top
    tempTop = top
    top = top - 1
    return arrayNum[tempTop]
    

word = input('Enter a word: ')
if len(word) <= 10:
    for i in range (0,len(word)):
        pushItem(word[i])

sameLetters = 0
for i in range (0, len(word)):
    if popItem() == word[i]:
        sameLetters += 1
print(sameLetters)

        
    
 