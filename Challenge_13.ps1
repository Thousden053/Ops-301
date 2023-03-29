#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 13
# Purpose:        Creates user in AD
# Why:            Creating user's is tedious so why not automate it?


#Main

Import-Module ActiveDirectory

# Define the user properties
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$description = "TPS Reporting Lead at GlobeX USA in Springfield, OR office"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$username = "ferdinand"
$password = "P@ssw0rd"  # Replace with a strong password

# Define the path where to create the user account
$ouPath = "OU=Users,OU=GlobeX USA,DC=Corp,DC=globexpower,DC=com"  # Replace with your domain name

# Create the new user account
New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -Description $description `
    -Office $office -Department $department -EmailAddress $email -SamAccountName $username `
    -AccountPassword (ConvertTo-SecureString $password -AsPlainText -Force) -Enabled $true -Path $ouPath


#had help from chatgpt, not strong in PS.


#End