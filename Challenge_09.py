#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 09
# Purpose:        
# Why:     

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# Main


# 1st draft
# print("These were your entries:\n", "Entry 1: \n" ,a, "\n Entry 2: \n", b)

# try:
#     a = int(a)
# except ValueError:
#         print("That's not an integer. Please try again.")

# try:
#     b = int(b)
# except ValueError:
#         print("That's not an integer. Please try again.")

# try:
#     a = int(a)
#     print(f"You entered the integer: {a}")
# except ValueError:
#     print(a, " is not a valid integer.")

# try:
#     b = int(b)
#     print(f"You entered the integer: {b}")
# except ValueError:
#     print(b, " is not a valid integer.")


#2nd draft
import sys

def integer_input(prompt):
    while True:
        user_input = input(prompt)
        
        try:
            return int(user_input)
        except ValueError:
            print("The input is not an integer. Please try again.")

a = integer_input("Please enter the first integer: ")
b = integer_input("Please enter the second integer: ")

if a == b:
    print (a, " and ", b, "are equivalent")
elif a != b:
    print (a, " and ", b, "are not equivalent")
else:
    print ("Error")

if a < b:
    print(a ," is less than ", b)
elif a <= b:
    print(a ," is less than or equal to", b)
else:
    print(a ," is greater than or equal to",b )






# End