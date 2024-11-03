def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the position for Fibonacci series: "))
for i in range(num):
    print(fibonacci(i), end=" ")

# LOGIC EXPLANATION:

# What is the Fibonacci Series?
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones. The sequence typically starts with 0 and 1, like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number in the series (after the first two) is found by adding the two numbers just before it.

# Code Explanation
# Defining the Fibonacci Function:

# def fibonacci(n):
# This defines the fibonacci function, which takes an integer n as input. It will return the Fibonacci number at position n.

# Base Cases (Stopping Conditions):

# if n <= 0:
#     return 0
# elif n == 1:
#     return 1
# If n is 0, the function returns 0, as the 0th Fibonacci number is 0.
# If n is 1, it returns 1, as the 1st Fibonacci number is 1.
# These are the base cases that stop the recursion from going infinitely.

# Recursive Case:

# else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
# If n is greater than 1, the function calls itself twice: once with n - 1 and once with n - 2. This means it adds the two previous Fibonacci numbers together to get the next one. This is the core idea behind the Fibonacci series.

# Getting User Input and Displaying the Fibonacci Series:

# num = int(input("Enter the position for Fibonacci series: "))
# for i in range(num):
#     print(fibonacci(i), end=" ")
# This part takes an integer input from the user, num, which represents the number of Fibonacci numbers to display.
# It uses a for loop to calculate and print each Fibonacci number from 0 to num - 1 by calling fibonacci(i).
  
# Example Walkthrough
# Suppose the user inputs 5.

# fibonacci(0) returns 0
# fibonacci(1) returns 1
# fibonacci(2) calls fibonacci(1) + fibonacci(0) and returns 1 + 0 = 1
# fibonacci(3) calls fibonacci(2) + fibonacci(1) and returns 1 + 1 = 2
# fibonacci(4) calls fibonacci(3) + fibonacci(2) and returns 2 + 1 = 3
# So, the output would be:

# 0 1 1 2 3
