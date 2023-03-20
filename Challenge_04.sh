#!/bin/bash

# Script:         Ops 301 Ops Chall 04
# Purpose:        Prints file size of file, then compresses and shows file size after compression
# Why:            Compression is a useful tool to save valuable storage space.

#Main

#establishes variables for file paths to reduce excess code.
backup_dir="/var/log/backups"
syslog="/var/log/syslog"
wtmp="/var/log/wtmp"

# creats directory
mkdir -p "$backup_dir"

#establishes function 
process_file() {
  file="$1"
  timestamp=$(date +"%Y%m%d%H%M%S")
  zip_name="$backup_dir/$(basename "$file")-$timestamp.zip"
  #du -h makes the output of disk usage human readable
  size_before=$(du -h "$file")
  #compresses file in zip format and truncates 
  zip -r "$zip_name" "$file" && truncate -s 0 "$file"
  size_after=$(du -h "$zip_name")
  
  echo "Size Before: $size_before, Size After: $size_after"
}

process_file "$syslog"
process_file "$wtmp"


# code generated by chatgpt to help understand, I was a little confused with how to structure.
#End