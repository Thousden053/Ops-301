#!/bin/bash

for (( i=5; i<=14; i++ ))
do
    if [ $i -lt 10 ]; then
        touch Challenge_0$i.sh
    else
        touch Challenge_$i.sh
    fi
done
