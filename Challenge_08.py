#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 08
# Purpose:        Uses a list to hold values rather than assigning individual variables.
# Why:            Groups variables into a list, and assigns them place values to call upon one or multiple when needed.

#Main

#Establishes list and inserts values
List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#Outputs all values in list defined above
print(List)

#Outputs the 4th object in list, remember 0 is the 1st object.
print(List[3])
#Outputs the 6th through 10th value in the list
print(List[5:9])

#Changes the 7th value in the defined list to "onion"
List[6] = "onion"

#Outputs the defined list
print(List)

#End