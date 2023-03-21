#!/bin/bash

for (( i=8; i<=14; i++ ))
do
    if [ $i -lt 10 ]; then
        touch Challenge_0$i.py
    else
        touch Challenge_$i.py
    fi
done
