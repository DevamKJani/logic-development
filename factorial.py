def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial (x - 1)
        
num = int(input("enter number: "))
z = factorial(num)
print("factorial of", num, "is", z)

# LOGIC EXPLANATION

# Defining the Factorial Function:

# def factorial(x):
# This defines a function called factorial that takes an integer x as input.

# Base Case (Stopping Condition):

# if x == 0 or x == 1:
#     return 1
# Here, we check if x is either 0 or 1. If it is, we know the factorial of 0 or 1 is 1, so the function returns 1 immediately without further calculations. This is the base case in recursion and helps the function stop.

# Recursive Case:

# else:
#     return x * factorial(x - 1)
# If x is greater than 1, the function calls itself with the value x - 1. For example, if x is 5, it returns 5 * factorial(4). This call then continues to break down until it reaches 1.

# Calculating Factorial:

# num = int(input("enter number: "))
# This line takes a number as input from the user and stores it in the variable num.

# Executing the Factorial Function:

# z = factorial(num)
# This line calls the factorial function with the user's input (num) and stores the result in z.

# Displaying the Result:

# print("factorial of", num, "is", z)
# This line prints the result of the factorial calculation.

# Simple Example of How It Works
# Let's say you enter 3 as the input.

# factorial(3) is called:
# It checks if 3 is 0 or 1 (it's not), so it goes to the else statement.
# It returns 3 * factorial(2).
# Then factorial(2) is called:
# It checks if 2 is 0 or 1 (it's not), so it goes to the else statement.
# It returns 2 * factorial(1).
# Then factorial(1) is called:
# This time 1 matches the base case, so it returns 1.
# Now, putting it all together:

# factorial(3) returns 3 * 2 * 1, which is 6.
