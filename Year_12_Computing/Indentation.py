'''Challenge: 
 correct the indentation to follow Python's standard indentation rules. Note that indententation makes code more readable and therfore easier to maintain. '''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_user_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Please enter a valid integer.")

def main():
    number = get_user_input()
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

if __name__ == "__main__":
    main()