#Write a program that calculates the factorial of a given number. ---> (COPMPLETED )
#Define a function called factorial that takes an integer as input and returns its factorial. ---> (COPMPLETED ) 
#Call this function to compute the factorial of a number entered by the user ---> (COPMPLETED )

#defining a function called factorial()
def factorial():
    factorial_num = 1
    #inputting number
    num = int(input('Enter a number: '))
    #for loop
    for i in range (1,num+1):
        #multilpyig each i by the next i
        factorial_num = factorial_num*i
     #returning factroial 
    return factorial_num

#calling funtion and printing returned value
print(factorial())
