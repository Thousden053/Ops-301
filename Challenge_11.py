#!/usr/bin/env python3

# Script:         Ops 301 Ops Chall 11
# Purpose:        
# Why:     

#Main

#imports psutil which allows access and retrieval of system info

import psutil

# sets cpu_times function to obtain cpu times for the system
cpu_times = psutil.cpu_times()

#establishes logs tuple formatted as a string using "f" before the string
logs = (
    (f"Time by normal processes executing in user mode: {cpu_times.user:.2f} seconds"),
    (f"Time by processes executing in kernel mode: {cpu_times.system:.2f} seconds"),
    (f"Time when system was idle: {cpu_times.idle:.2f} seconds"),
    (f"Time by priority processes executing in user mode: {psutil.cpu_times(percpu=True)[0].user:.2f} seconds"),
    (f"Time waiting for I/O to complete: {cpu_times.iowait:.2f} seconds"),
    (f"Time for servicing hardware interrupts: {cpu_times.irq:.2f} seconds"),
    (f"Time for servicing software interrupts: {cpu_times.softirq:.2f} seconds"),
    (f"Time by other operating systems running in a virtualized environment: {cpu_times.guest:.2f} seconds"),
    (f"Time running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest_nice:.2f} seconds")
)

#sets for loops to print each tuple established above.
for log in logs:
    print(log)


#End