#!/bin/bash

# Script:         Ops 301 Ops Chall 02
# Purpose:        Append, date and time
# Why:            It's important to know how to time stamp your documents for record purposes.

# Main

# prompts user for directory path
echo "Input directory path"
# records user input as path var
read path
# prompts user for permissions they want to add to file or entire directory
echo "Input desired permissions"
# records user input as perm var
read perm
# runs chmod commaand with -R flag (recursive)
chmod -R $perm $path
# prints contents of directory saved in path var and their permissions with -al flag
ls -al $path

# End