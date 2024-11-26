'''Create a Class for a Student
⭐⭐⭐⭐

Challenge: 
Develop a Python class for a Student. 
The constructor should take parameters for the student's name, ID, and university major.
 Implement private attributes for these parameters. Create methods to get and set the student's major, 
 as well as to display the student's information. 

Instantiate more than one object from the class, and show suitable testing.  '''

class Student:
    # set private attributes
    __studentName = None
    __id = None
    __universityMajor = None
    # constructor method
    def __init__(self, theStudentName, theId, theUniversityMajor):
        self.__studentName = theStudentName
        self.__id = theId
        self.__universityMajor = theUniversityMajor
    # method to get university major
    def getUniversityMajor(self):
        return self.__universityMajor
    # method to set university major    
    def setUniversityMajor(self,theUniversityMajor):
        self.__universityMajor = theUniversityMajor
    # method to display all information  
    def displayInformation(self):
        print(self.__studentName, self.__id, self.__universityMajor)

#################################### --> Main Program <-- ######################################
# instantiating objects student1 and student2 using the class Student
student1 = Student('Eesa', 1416, 'Computing')
student2 = Student('Husaam', 1234, 'English')

# using mehtod to dispplay inforamtion of both objects
student1.displayInformation()
student2.displayInformation()

# using method to set and get university major 
student1.setUniversityMajor('Maths')
student1.displayInformation()
if student1.getUniversityMajor() == 'Maths':
    print('You are not doing a computing degree')


