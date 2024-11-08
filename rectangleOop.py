'''Create a Class for a Rectangle
⭐⭐⭐⭐

Challenge: 
Define a Python class for a Rectangle. The constructor should take parameters for the length and width of the rectangle.
 Implement private attributes for these parameters. Create methods to calculate the area and perimeter of the rectangle.

Instantiate more than one object from the class, and show suitable testing.  '''

class Rectangle:
    # set private attributes
    __length = None 
    __width = None
    # contructor method
    def __init__(self, theLength, theWidth):
        self.__length = theLength
        self.__width = theWidth
    # method to return area
    def calculateArea(self):
        return(self.__length * self.__width)
    # method to return perimeter       
    def calculatePerimeter(self):
        return((2 * self.__length) + (2 * self.__width))

################################################
        
# instantiating 3 objects using Rectangle class
rectangle1=Rectangle(-4,4)
rectangle2=Rectangle(10,10)
rectangle3 = Rectangle(10.5,20.5)

# outputting are and perimeter
print(rectangle1.calculateArea())
print(rectangle1.calculatePerimeter())
print('')
print(rectangle2.calculateArea())
print(rectangle2.calculatePerimeter())
print('')
print(rectangle3.calculateArea())
print(rectangle3.calculatePerimeter())