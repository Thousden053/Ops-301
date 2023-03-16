#!/bin/bash

# Script:         Ops 301 Ops Chall 02
# Purpose:        Append, date and time
# Why:            It's important to know how to time stamp your documents for record purposes.

# Main
cp /var/log/syslog ./


# Outputs Year, Month, Day respectively
echo `date +%Y`
echo `date +%m`
echo `date +%d`

# establishes variables for Y,m,d date flags
year=`date +%Y`

echo $year

month=`date +%m`
echo $month

day=`date +%d`
echo $day

# establishes variables for H,M,S date flags
hr=`date +%H`
echo $hr
min=`date +%M`
echo $min
sec=`date +%S`
echo $sec

#combines variables to create a complete date

echo "Today's Date: $day-$month-$year"
echo "Current Time: $hr:$min:$sec"


# displays contents of code.txt
echo "File before append: "
cat code.txt

echo "This is the time: `date`" >> newcode.txt
echo -e "\nAppended file:" 
cat newcode.txt

# End




