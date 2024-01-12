# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Marco Aleman
# maalema2@uci.edu
# 84703651


print("Welcome to the ICS 32 Calculator\n")

num_1 =  int(input("Input your first number: "))
num_2 = int(input("Input your second number: "))

opp = input("Input an operator (+, -, or x): ")

while opp != "+" and opp != "-" and opp != "x":
    opp = input("Please input a valid response: ")

if opp == "+":
    add = num_1 + num_2
    print(f'Your answer is {add}')
elif opp == "-":
    min = num_1 - num_2
    print(f'Your answer is {min}')
elif opp == "x":
    mult = num_1 * num_2
    print(f'Your answer is {mult}')
