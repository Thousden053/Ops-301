#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 10
# Purpose:        
# Why:     


# Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.
#Main


# newfile = open("test.txt", "w")

# # How to open a file
# openfile = open("test.txt")

# # How to return the five first characters of a file
# read = open("test.txt", "r")
# print("test.txt"(readline(1))



# Opens a new file named in test.txt in write mode and appends three lines
with open("test.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Opens the file in read mode and print the 
with open("test.txt", "r") as file:
    for i in range(3):
        line = file.readline()
        print(line)

# Delete the file
import os
os.system("rm test.txt")
# #End