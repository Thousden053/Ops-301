#!/bin/bash

for (( i=5; i<=14; i++ ))
do
    if [ $i -lt 10 ]; then
        touch challenge_0$i.sh
    else
        touch challenge_$i.sh
    fi
done
