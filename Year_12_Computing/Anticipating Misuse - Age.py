#Write a program that asks the user to input their age and calculates the year they were born. --> (COMPLETED)
#Handle potential misuse such as entering non-numeric characters or negative values as age input. -->  (COMPLETED) 
#Display a friendly error message in case of invalid input. --> (COMPLETED) 

#initialising the variable counter as a variable that will exit the loop if all validations are passed
counter = 0
# entering the loop which will check age is a positive integer
while not counter == 2:
    # imputting age and setting counter to 0
    counter = 0
    age = input('Please enter your age: ')
    # checking if age is an integer
    try:
        age=int(age)
       # counter = 1 once age is integer
        counter = counter + 1    
    except ValueError:
        print('Please enter your age as a numercial value: ')
    # once age is an integer, checking age is postive 
    if counter == 1:
        if age<0:
            print('Enter a value greater than 0')
        else:
            counter = counter + 1

# importing year from datetime
from datetime import datetime
current_year = datetime.now().year
# subtracting year and age and output
print('You were born in the year '+ str(current_year-age))








