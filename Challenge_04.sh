#!/bin/bash

# Script:         Ops 301 Ops Chall 03
# Purpose:        Creates a menu for a user to select different options, and the code will perform until the user selects the exit option.
# Why:            Familiarizes us with how simple menu's are made with code.

# Main

#Sets counter for loop
cont_var=1
# establishes loop, as long as the variable's value is 1 it will continuously run.
while [ $cont_var -eq 1 ]; do
# Starts the menu code, by displaying options and asking for entry.
    echo -e "Please select an option: \n(Enter the number only)  \n1: Hello World \n2: Ping Self \n3: IP info \n4: End"
    #records entry and assigns value to a variable.
    read entry
    #conditional to compare user entry with menu option's
    if [ $entry -eq 1 ]; then
        echo "Hello World"
    elif [ $entry -eq 2 ]; then
        echo "Enter your IPv4 address"
        read address
        # -c flag limits ping transmissions to # of lines specified by number after -c then stops ping
        ping -c 4 $address
    elif [ $entry -eq 3 ]; then
        ip a
    elif [ $entry -eq 4 ]; then 
        cont_var=0
    else
        echo "Invalid option, try again"
    fi
done

#End