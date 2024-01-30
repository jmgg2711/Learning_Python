# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:18:07 2024

@author: jgutierr2
"""

#region Datatypes
# ---- Datatypes
# b) Data types

# In Python, data types are used to define the type of data that a variable can hold. There are several build-in data
# types in Python, including:
#   Integer: An integer is a whole number with no decimal points, For example 1, 2, 3 and so on are all integers.
#   In Python, you can declare an integer by assigning a number to a varibale, like this:
x = 5

#   Float: A float is a number with a decimal point. For example 1.0, 2.5, and 3.14 are all floats. In Python, you can
#   declare a float by assigning a number with a decimal point to a variable, like this:
y = 3.14
y2 = 1.0

#   String: A string is a sequence of characters. In Python, you can declare a string by closing a sequence of
#   characters in single quotes ('...') or double quotes ("..."). For example:
z = 'hello'
z2 = "hello"

#   Boolean: A boolean is a data type that can only have two values: True or False. In Pytho, you can declare a boolean
#   by assigning the value True or False to a variable, like this:
a = True

# In Python, you can perform various mathematical operations on different data types, such as numbers, strings, lists,
# and tuples.

# Here are some basic mathematical operations for the first 4 datatypes in Python:

# Integer:
x = 2
y = 3
z = x + y   # Addition
print(z)    # Output: 5

z = x - y   # Substraction
print(z)    # Output: -1

z = x * y   # Multiplication
print(z)

x = 6
y = 3
z = x / y   # Division
print(z)    # Output: 2.0
print(type(z))  # Output: float

x = 7
y = 3
z = x // y  # Integer division
print(z)    # Output: 2

x = 7
y = 3
z = x % y   # Modulus
print(z)    # Output: 1 

x = 2
y = 3
z = x ** y  # Exponentiation
print(z)    # Output: 8

# If you want to perform a mathematical operation on the value of an already existing varibale, there are some shortcuts
x = 1
x += 2      # same as: x = x + 2
x *= 2      # same as: x = x * 2
x /= 2      # same as: x = x / 2
x **= 2     # same as: x = x ** 2
x //= 2     # same as: x = x // 2
x %= 2      # same as: x = x % 2
# What is x? x = 0

# Floats
# The same mathematical operations as for the integer datatype apply for the float datatype as well. The output will
# always be a float datatype, even if an integer is involved:
x = 2       # integer
y = 3.0     # float
z = x * y
print(z)    # Output: 6.0 (float)

# Strings:
x = 'Hello'
y = "world"
z = x + " " + y     # Concatenation
print(z)            # Output: Hello world

z = x * 3   # Multiplication
print(z)    # Output: HelloHelloHello

# Boolean:
x = True
y = False
z = x and y     # same as z = x & y
print(z)        # Output: False

z = x or y      # same as z = x | y 
print(z)h        # Output: True

z = not x       # Output: False

z = x == y      # Check if x equal y
print(z)        # Output: False
    
z = x != y      # Check if x unequal y
print(z)        # Output" True

# Be careful with logic operations! Brackets are recommended for complex operations:
z = (not(x and y)) and (not((not x) and (not y)))
print(z)

# None
# None> does not support any mathematical operation, as it represents the absence of a value
a = None
b = 10
print(a + b)    # TypeError: unsopported operand type(s) for +: 'Nonetype' and 'int'

#endregion

b = "!Hola, Mundo"
print(b[2:5])
print(b[2:])
print(b[:5])
print(b[-5:-2])


