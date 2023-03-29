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



#enables use of requests in python
import requests 

#user input
url = input("Please enter a URL: \n")
#compares user input with following strings, if either are not in the input then they will be added. 
#I wanted to make cover typo's, but spent too much time on the code already.
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

#establishes list for later use
options = ["GET","POST","PUT","DELETE","HEAD","PATCH","OPTIONS"]

#establishes counter for while loop
counter = 1
#establishes while loop to correct user error
while counter < 2:
    #user input
    print("You're about to perform an HTTP request. Please select an option:")
    #for loop to print all items in the list "options"
    for item in options:
        print(item)
    #user input (.upper() used to conver input to upper for matching to list.)
    response = input("Enter an HTTP method: ").upper()
    #checks if response matches a value in list "options"
    if response in options:
        print("Your response was:", response)
    else:
        print("Invalid HTTP method. Please try again.")
       
    #counter for 2nd while loop.
    counter2 = 1
    #2nd while loop to correct user error.
    while counter2 < 2:
        #user input (.lower() converts input to lower case for matching to strings defined in if, elif)
        verify = input("Would you like to continue with your request? (Yes/No)\n").lower()
        if verify == "yes":
            #assigns http request command to variable "method"
            method = requests.request(response, url)
            #assigns the status code output of the http request to var "status_code"
            status_code = method.status_code
            #verifies if the status_code output matches any of the below given status codes and will print to screen whichever matches.
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
            elif status_code == 405:
                status_text = 'Invalid Request'
            elif status_code == 500:
                status_text = 'Internal Server Error'
            print("Response status code:", status_code, "-", status_text)

            #3rd while loops to correct user error.
            
            while counter2 < 2:
                cont = input("Would you like to perform another request? (Yes/No)\n").lower()
                if cont == "yes":
                    counter2 = 2
                elif cont == "no":
                    print("You've chosen to cancel, Goodbye.")
                    counter = 3
                    counter2 = 3
                else:
                    print("Invalid input. Please enter 'Yes' or 'No'.")
                    counter3 = 2
        elif verify == "no":
            print("You've chosen to cancel, Goodbye.")
            counter = 3
            counter2 = 3
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
    
