#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 07
# Purpose:        
# Why:            

#Main
import os 

path = input("Please enter a file path\n")

for (root, dirs, files) in os.walk(path):
  
    print("Root:", root)
    
    print("Directories: ", dirs)
  
    print("Files: ", files) 