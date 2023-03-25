#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 09
# Purpose:        Asks user for input of integers, verifies the inputs are integers then compares the inputs
# Why:            Comparing values is useful for small to large values.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# Main

#1st draft of function
# def integer_input(prompt):
#     while True:
#         user_input = input(prompt)
        
#         try:
#             return int(user_input)
#         except ValueError:
#             print("The input is not an integer. Please try again.")

# defines function with nested try/ return to verify if the input is an integer.
# try/return is done by taking user input and trying to convert to integer, if it is possible code will continue. 
# If not able to convert to int,user will be told to try again until int is given

def integer_input(prompt):
    while True:
        
        try:
           user_input = int(input(prompt))
           return user_input
        except ValueError:
            print("The input is not an integer. Please try again.")

#assigns the function above to two variables. 
a = integer_input("Please enter the first integer: ")
b = integer_input("Please enter the second integer: ")
#used to compare the two integers values given by user
if a == b:
    print (a, " and ", b, "are equivalent")
elif a != b:
    print (a, " and ", b, "are not equivalent")
    if a < b or a <= b:
        print(a ," is less than or equal to", b)
    else:
        print(a ," is greater than or equal to",b)
else:
    pass 






# End