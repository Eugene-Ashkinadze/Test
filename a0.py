# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Eugene Ashkinadze
# eashkina@uci.edu
# 36928353
lines = int(input())

endline = lines - 1
for i in range(lines):
    if i == 0:
        print("+-+")
        print("| |")
        print("+-", end='')
    elif i == endline:
        print("+-+")
        print(" " * (i*2) + "| |")
        print(" " * (i*2) + "+-+")
    else:
        print("+-+")
        print(" " * (i*2) + "| |")
        print(" " * (i*2) + "+-", end = '')