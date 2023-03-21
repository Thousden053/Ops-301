#!/bin/bash

# for (( i=5; i<=14; i++ ))
# do
#     if [ $i -lt 10 ]; then
#         touch Challenge_0$i.sh
#     else
#         touch Challenge_$i.sh
#     fi
# done

for i in {01..05}; do
  old_file="Challenge_$i.sh"
  next_num=$(printf "%02d" $((10#$i + 1)))
  new_file="Challenge_$next_num.sh"

  if [ -e "$old_file" ]; then
    mv "$old_file" "$new_file"
    echo "Renamed $old_file to $new_file"
  else
    echo "File $old_file not found"
  fi
done
