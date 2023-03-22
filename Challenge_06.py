#!/usr/bin/env python3

# # How to use Linux/Bash commands within Python
# # First import the os library
# import os

# # Then use os.system to call any kind of bash command
# os.system("ls")

# # Here are some Python-specific operations for you to practice
# # How to print to terminal
# print("Welcome to Python!")

# # How to declare a variable
# var_greeting = "Welcome to Python!"

# # How to call a variable
# print(var_greeting)

# Main 

#configure python to interpret host os language
import os

#defines 3 variable with scripts from host os language (in this case bash)
var1=os.system("whoami")
var2=os.system("ip a")
var3=os.system("lshw -short")
var4=4
#prints defined variables to screen
print ("Running command: ", var1)
print (var2)
print (var3)
print (var4)
#End