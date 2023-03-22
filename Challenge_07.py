#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 07
# Purpose:        Displays contents of a file path
# Why:            Good for retrieving information about directories and contents within.

#Main
import os 
# assigns the users input as variable "path"
path = input("Please enter a file path\n")

#uses a for loop to detect root, dirs, and files in the variable command.
for (root, dirs, files) in os.walk(path):
  
    print("Root:", root)
    
    print("Directories: ", dirs)
  
    print("Files: ", files)

    #End