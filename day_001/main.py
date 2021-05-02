# First Lesson - print() statements
print("100 Days of Python - Day 1")
print("==========================")
print("")

# Exercise 1-1 - Printing
print(
    """Day 1 - Python Print Function
The function is declared like this:
print('what to print')
"""
)

# Exercise 1-2 - Debugging
# Fix the code below 👇
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 1-3 - Input Function
# Solution:
# input() will ask for the users name
# then len() will calculate the length of the input
# the result of len() then get's printed to the console through the print() function
print(len(input("What's your name?: ")))

# Exercie 1-4 - Variables
# Write a program that switches the values stored in the variables a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Using one switch-variable
x = a
a = b
b = x


# Using two additional variables
# x, y = a, b
# b, a = x, y

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Variable Namings
# Good practices for Variable Namings:
# Use Snake_Case for variable names with multiple words
# e.g. user_name, user_password, date_of_birth, side_length ...
# Numbers can be appended to variable names, but never prefixed
# Good: number1, number2
# Bad: 1number, 2number
