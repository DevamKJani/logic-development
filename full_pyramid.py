def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)

# CODE EXPLANATION:

# def full_pyramid(n):
#     for i in range(1, n + 1):
# Function Definition:
# full_pyramid(n) is a function that takes n (the number of rows) as input.
# The outer loop (for i in range(1, n + 1)) iterates from 1 up to n, where i represents the current row number (starting from 1).
# Generating Leading Spaces for Each Row

#         for j in range(n - i):
#             print(" ", end="")
# Leading Spaces:
# For a full pyramid pattern, each row needs a certain number of spaces before the asterisks to align the pattern as a pyramid.
# In row i, the number of leading spaces needed is n - i.
# This inner loop (for j in range(n - i)) prints " " (a space) multiple times without a newline (end=""), creating the necessary indentation for each row.
# Printing Asterisks for Each Row

#         for k in range(1, 2 * i):
#             print("*", end="")
# Asterisks:
# After printing the leading spaces, the next inner loop (for k in range(1, 2 * i)) prints asterisks (*) to form the pyramid shape.
# The number of asterisks required for row i is 2 * i - 1 to keep the pyramid symmetrical.
# This loop also avoids a newline after each asterisk by using end="".
# Moving to the Next Row
#         print()
# After each row is completed (spaces and asterisks printed), print() without any arguments creates a newline, moving to the next row.
# Example Walkthrough
# For n = 5, the function will output:

#     *
#    ***
#   *****
#  *******
# *********
# Explanation for Each Row
# Row 1 (i = 1): n - i = 4 spaces, 2 * i - 1 = 1 asterisk


#     *
# Row 2 (i = 2): n - i = 3 spaces, 2 * i - 1 = 3 asterisks


#    ***
# Row 3 (i = 3): n - i = 2 spaces, 2 * i - 1 = 5 asterisks


#   *****
# Row 4 (i = 4): n - i = 1 space, 2 * i - 1 = 7 asterisks


#  *******
# Row 5 (i = 5): n - i = 0 spaces, 2 * i - 1 = 9 asterisks


# *********

#########################################################################################################################################

# Code Execution Breakdown for n = 5
# The goal is to generate a pyramid with 5 rows, where each row is centered with spaces and has an increasing number of asterisks.


# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
   
# full_pyramid(5)
# Step-by-Step Execution for Each Row
# Row 1 (i = 1)
# Leading Spaces: n - i = 5 - 1 = 4 spaces.
# Asterisks: 2 * i - 1 = 2 * 1 - 1 = 1 asterisk.
# So, Row 1 looks like this:


#     *
# Row 2 (i = 2)
# Leading Spaces: n - i = 5 - 2 = 3 spaces.
# Asterisks: 2 * i - 1 = 2 * 2 - 1 = 3 asterisks.
# Row 2 will look like this:


#    ***
# Row 3 (i = 3)
# Leading Spaces: n - i = 5 - 3 = 2 spaces.
# Asterisks: 2 * i - 1 = 2 * 3 - 1 = 5 asterisks.
# Row 3 will look like this:


#   *****
# Row 4 (i = 4)
# Leading Spaces: n - i = 5 - 4 = 1 space.
# Asterisks: 2 * i - 1 = 2 * 4 - 1 = 7 asterisks.
# Row 4 will look like this:


#  *******
# Row 5 (i = 5)
# Leading Spaces: n - i = 5 - 5 = 0 spaces.
# Asterisks: 2 * i - 1 = 2 * 5 - 1 = 9 asterisks.
# Row 5 will look like this:


# *********
# Final Output
# When combined, the complete output will be:


#     *
#    ***
#   *****
#  *******
# *********
# Explanation Summary
# Spaces: For each row i, we print n - i spaces to create the centered effect.
# Asterisks: For each row i, we print 2 * i - 1 asterisks, increasing by 2 each row to keep the pyramid shape.
