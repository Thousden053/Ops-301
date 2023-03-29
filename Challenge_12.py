#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 07
# Purpose:        
# Why:     

# Main

# import requests 

# url =input("Please enter a URL: \n")
# if not url.startswith('http://') and not url.startswith('https://'):
#     url = 'http://' + url
# options = ["GET","POST","PUT","DELETE","HEAD","PATCH","OPTIONS"]

# counter = 1
# while counter < 2:
# # # establishes counter for loop, as long as the variable's value is 1 it will continuously run.
# # while cont_var=1:
# # Starts the menu code, by displaying options and asking for entry.
#     print("You're about to perfrom an HTTP request.")
#     for item in options:
#         print (item)
#     response =input("Please select an option: \n")
#     response = response.upper()
#     if response in options:
#         print ("Your response was: ", response)
#     else:
#         print ("Your response was: ", response, "please try again.")
#     counter2 = 1
#     while counter2 < 2:
#             verify = input("Would you like to continue with your request? (Yes/No)\n")
#             verify = verify.lower()
#             if verify == "yes":
#                 method = requests.request(response, url)
#                 status_code = method.status_code
#                 if status_code in requests.status_codes.codes:
#                     status_code = method.status_code
#                 status_text = ''
#                 if status_code == 200:
#                     status_text = 'OK'
#                 elif status_code == 201:
#                     status_text = 'Created'
#                 elif status_code == 400:
#                     status_text = 'Bad Request'
#                 elif status_code == 401:
#                     status_text = 'Unauthorized'
#                 elif status_code == 404:
#                     status_text = 'Not Found'
#                 elif status_code == 500:
#                     status_text = 'Internal Server Error'
#                 print("Response status code:", status_code, "-", status_text)
#                 cont = input("Would you like to perform another request?\n")
#                 cont = cont.lower()
#                 counter2 += 1  
#             elif verify == "no":
#                 print("You've chosen to cancel, Goodbye.")
#                 counter = 2
#                 counter2 = 2
#             elif verify != "yes" or "no":
#                 print("Please enter yes or no")
#             counter3 = 1
#             while counter3 < 2:
#                 cont = input("Would you like to perform another request?\n")
#                 cont = cont.lower()
#                 if cont == "yes":
#                         counter = 1
#                 elif cont != "yes" or "no":
#                             print("Please enter yes or no")
#                 elif cont == "no":
#                     print("You've chosen to cancel, Goodbye.")
#                     counter3 == 2
    

#I created the entire code above, but could not figure out why it wouldn't loop back to "would you like to perform another request" line.
#Chat gpt didn't help when I asked. Figured it out to be that i incorrectly set the counters
#Chat GPT helped with the  "method = requests.request(response, url) status_code = method.status_code" part of the code.

import requests 

url = input("Please enter a URL: \n")
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

options = ["GET","POST","PUT","DELETE","HEAD","PATCH","OPTIONS"]

counter = 1
while counter < 2:
    print("You're about to perform an HTTP request. Please select an option:")
    for item in options:
        print(item)

    response = input("Enter an HTTP method: ").upper()
    if response in options:
        print("Your response was:", response)
    else:
        print("Invalid HTTP method. Please try again.")
        continue

    counter2 = 1
    while counter2 < 2:
        verify = input("Would you like to continue with your request? (Yes/No)\n").lower()
        if verify == "yes":
            method = requests.request(response, url)
            status_code = method.status_code
            if status_code in requests.status_codes.codes:
                status_code = method.status_code
            status_text = ''
            if status_code == 200:
                status_text = 'OK'
            elif status_code == 201:
                status_text = 'Created'
            elif status_code == 400:
                status_text = 'Bad Request'
            elif status_code == 401:
                status_text = 'Unauthorized'
            elif status_code == 404:
                status_text = 'Not Found'
            elif status_code == 500:
                status_text = 'Internal Server Error'
            print("Response status code:", status_code, "-", status_text)

            counter2 = 1
            while counter2 < 2:
                cont = input("Would you like to perform another request? (Yes/No)\n").lower()
                if cont == "yes":
                    counter2 = 1
                elif cont == "no":
                    print("You've chosen to cancel, Goodbye.")
                    counter = 2
                    counter2 = 2
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
                    counter2 = 1
        elif verify == "no":
            print("You've chosen to cancel, Goodbye.")
            counter = 2
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")



   

# #records entry and assigns value to a variable.
# #conditional to compare user entry with menu option's
# if [ $entry -eq 1 ]; then
#     print "Hello World"
# elif [ $entry -eq 2 ]; then
#     print "Enter your IPv4 address"
#     read address
#     # -c flag limits ping transmissions to # of lines specified by number after -c then stops ping
#     ping -c 4 $address
# elif [ $entry -eq 3 ]; then
#     ip a
# elif [ $entry -eq 4 ]; then 
#     cont_var=0
# else
#     print "Invalid option, try again"
    
