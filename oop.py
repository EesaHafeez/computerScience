class Dog:
    # private name
    Name = ''
    # private color
    Colour = ''

    # public constructor
    def __init__(self,theName, theColour):
        self.name = theName
        self.colour = theColour
    # public bark method
    def bark(barkTimes):
        for i in range(barkTimes):
            print('Woof')
    # public setColour method
    def setColour(self,theColour):
        self.colour = theColour
    # public getColour method
    def getColour(self):
        return self.colour
    # public setName method
    def setName(self,theName):
        self.name = theName
    # public getName method
    def getName(self):
        return self.name
##############################################################################################
myDog3 = Dog('Mutt','Unknown')
myDog4 = Dog('Jeff', 'Unknown')

'''print(myDog3.getName())
myDog3.setName(input('Enter a new name for myDog3: '))
print(myDog3.getName())
print('')

print(myDog4.getName())
myDog4.setName(input('Enter a new name for myDog4: '))
print(myDog4.getName())
print('')


print(myDog3.getColour())
myDog4.setColour(input('Enter a new colour for myDog3: '))
print(myDog4.getColour())
print('')

print(myDog3.getColour())
myDog4.setColour(input('Enter a new colour for myDog4: '))
print(myDog4.getColour())
print('')'''

myDog4 = myDog3
print(myDog3)
print(myDog3)
print(myDog4.getName())
