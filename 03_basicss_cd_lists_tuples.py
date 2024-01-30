# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:23:44 2023

@author: jgutierr2
"""

#region Tuples
# ---- Tuples
# In Python, both lists and tuples are used to store collection of items, but there are some differences between them.
#
# A list is a mutable object, which means that it can be modified after it has been created. Elements can be added,
# removed or changed, and the length of the listcan be changed. A list is created using square brackets [] and the 
# elements are separated by commas.
#
# On the other hand, a tuple is an inmutable object, which menad that it cannot be modifiedafter it has been created.
# Elements cannot be added, removed or changed, and the length of the tuple cannot be changed. A tuple is created using
# round brackets () and the elements are separated by commas.
my_tuple = (1, 2, 3, 4, 5)
#
# In general, a list is used when you have a collection of items that you want to modify or update, while a tuple is 
# used when you have a collection of items that you want to keep as is and do not need to change.

print(my_tuple[0])
my_tuple[0] = 10
my_tuple.append(6)

my_tuple = (2, 3, 4, 5)     # overwriting works
print(my_tuple)
#endregion

#region sets
# ---- Sets

# Python, a set is a collection of unique and unordered elements. This means that sets are a way to store a group of items,
# just like lists and tuples, but they don't allow for duplicates
#
# A set si defined using curly braces {} or the set() function, and items are separated by commas. Here is an example of
# creating a set of fruits:
fruits = ["banana", "orange", "apple", "grapes", "banana"]
print(fruits)
# Convert list to a set
set_of_fruits = set(fruits)
# Return a set into a list
list_of_fruits = list(set_of_fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.add(5)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

set2.remove(6)

# But who has time to remember all those keywords?
# You can also just use mathematical and logical opoerations (or = |) (and = &) on sets:
    
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 = set1 | {5}   # same as set.add(5)
union_set = set1 | set2 # same as set1.union(set2)
intersection_set = set1 & set2 # same as set1.intersection(set2)
difference_set =  set1 - set2 # same as set1.difference(set2)

# There is another operator for the symmetric difference. The symmetric difference between two sets A and B is a new
# set containing all the elements that are in either set A or set B but not in both. The symmetric difference operator
# if represented by the ^ symbol

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

#endregion

#region Set task
# ---- Set Task

# Task 1: Generate alsit of measurement parameters (or similar), which are common in your field of work 
# (IGSS(NEG) @ 20V,    VTH @ 2mA, IGSS @ 20V, VTH2 @ 2mA, IGSS2 @ 20V, VTH @ 18mA, RDON @ 4A 15V, RDON @ 105A 15V,    RDON @ 105A 18V, RDON @ 105A 20V)
sic_electrical_param = ["IGSS(NEG) @ 20V","VTH @ 2mA","IGSS @ 20V","VTH2 @ 2mA","IGSS2 @ 20V","VTH @ 18mA","RDON @ 4A 15V","RDON @ 105A 15V","RDON @ 105A 18V","RDON @ 105A 20V"]
# Task 2: Convert the list into a set
set_sic_electrical_param = set(sic_electrical_param)
# Task 3: Check if "VTH @ 2mA" is in your set and print the result
print("VTH2 @ 2mA" in set_sic_electrical_param)
# Task 4: Create a set of parameters, needed for a normalization set and the parameter set to find out if a parameter is still missing in your parameter set
normalization_param = set(["IGSS(NEG) @ 20V","VTH @ 2mA","IGSS @ 20V","VTH3 @ 2mA","IGSS2 @ 20V","VTH @ 18mA","RDON @ 4A 15V","RDON @ 105A 15V","RDON @ 105A 18V","RDON @ 105A 20V"])
# Task 5: Print out the difference of your normalization set and the parameter set to find out if a parameter is still missing in your parameter set
missing_parameters = normalization_param - set_sic_electrical_param
# Task 6: Add the following parameter to your set: "dummy_measurement"
set_sic_electrical_param.add("dummy_measurement")
# Task 7: Convert the set into a list and sort it alphabetically
params = sorted(list(set_sic_electrical_param))
# Task 8: Print out the number of parameters in your set
print(len(set_sic_electrical_param))

#endregion

#region Dictionaries
# ---- Dictionaries

#Dictionaries
# In Python, a dictionary is a data structure that stores key-value pairs. Think of it like a real-world dictionary,
# where you look up a word and find its definition.

# In Python dictionary, the key is like the word you are looking up, and the value is like the definition of that word.
# you can use any hashable object as a key (such as a string, number or tuple), and any object as a value.

# To create a dictionary, you use curly braces {}, and separate each key value pair with a colon : for example:
my_dict = {"Nombre": "Juan", "Apellido": "Gutierrez"}
# To access the value of a specific key in a dictionary, you use the key in square brackets. For example:
print(my_dict["Apellido"]) # output: "Gutierrez"

# You can also create an empty dictionary by using the dict() function, like this:
my_dict_empty =  dict()

# If you try to access a key that doesn't exist in the dictionary, you'll get a KeyError:
print(my_dict["Edad"])  # KeyError: 'Edad'

# to avoid the error, you can use:
print(my_dict.get("Edad"))  # prints None

# You can add or modify key-value pairs in a dictionary by assigning a value to a key:
my_dict["Edad"] = 46
my_dict["Fecha Nacimiento"] = "11/27/1976"
print(my_dict)

# Modifying a value 
my_dict["Edad"] = 47
print(my_dict)

# Delete an item from the dictionary
del my_dict["Fecha Nacimiento"]
print(my_dict)

# If you want to remove one key-value pair and use its value for further purposes, you can use the .pop method to pop
# it out of the existing dictionary:
my_dict = {"apple": 3, "banana": 5, "orange": 2}
apple_value = my_dict.pop("apple")
print(my_dict) # removes "apple" and keep {'banana': 5, 'orange': 2}
print(apple_value) # prints 3 (value obtained from 'apple')

# Dictionaries have the posibility to be automaticall updated with new information of a subpart of the original
# dictionary. The unused keys are not touched in the updating progress:
my_dict = {"apple": 3, "banana": 5, "orange": 2}
traded_fruits_dict = {"apple": 1, "dragonfruit": 2} # trade 2 apples for two dragonfruit
my_dict.update(traded_fruits_dict)
print(my_dict) # output: {'apple': 1, 'banana': 5, 'orange': 2, 'dragonfruit': 2}

# Often you need to check if a specific key is already existing within a dictionary. For that, the Keys() function
# will give you a dict_keys object of all keys within the dictionary in random order:
my_dict = {"apple": 3, "banana": 5, "orange": 2}
my_keys = my_dict.keys()
print(my_keys)  # output: dict_keys(['apple', 'banana', 'orange'])

#The dicts keys object is not directly a list, so you can not perform list operations on it:
my_keys[0]     #TypeError: 'dict_keys' object is not subscriptable

#But checking for specific values does work with the "in" / "not in" keywords:
print("apple" in my_keys)

# how we use it later on
"apple" in my_dict.keys()

# If you want to convert the dict_keys object to a list, use the list() function:
my_keys_as_list = list(my_keys)
print(my_keys_as_list)  # ['apple', 'banana', 'orange']
print(my_keys_as_list[0]) # apple

# The datatype of the assigned value is quite versatile. You can assign, int, float, str, bool, lists, tuples and dicts.
# This makes dictionaries very handy in storing program setting in a meaningful way, since the key provides
# information about the stored data.
# The definition can also be put into multiple lines for better readability:
my_setup_dictionary = {
    "switches":
        {
            "self_heating": True,
            "temperature_model": 2
        },
    "device": "hvn16p_ls",
    "offset": 1.3e-12,
    "stages": [1, 2, 3]
}
    
#endregion

#region Dictionary tasks
# ---- Dictionary tasks

# Task 1: Create an empty dictionary called plot_settings
plot_settings = dict()
plot_settings_alt = dict()
# Task 2: Add entries for title, x_label, y_label, is_logy, x_data (list), y_data (list)
plot_settings = {
    "title": "Isc: Short Circuit pulse",
    "x_label": "Time (us)",
    "y_label": "Current (A)",
    "is_log": False,
    "x_data": [0, 1, 2, 3, 4, 5],
    "y_data": [0, 3, 5, 8, 5, 3]
    }
# This is another way to resolve Task #2
plot_settings_alt["title"] = "Isc: Short Circuit pulse"
plot_settings_alt["x_label"] = "Time (us)"
plot_settings_alt["y_label"] = "Current (A)"
plot_settings_alt["is_log"] = False
plot_settings_alt["x_data"] = [0, 1, 2, 3, 4, 5]
plot_settings_alt["y_data"] = [0, 3, 5, 8, 5, 3]
# Task 3: Check if is_log is in the keys and print out the result
print("is_log" in plot_settings.keys())
# Task 4: make a new list in the form: [x_data, y_data]
new_list = [plot_settings["x_data"],plot_settings["y_data"]]
# Task 5: set is_logy to True
plot_settings["is_logy"] = True
# Task 6: print out a string containing: title-x_label-y_label
title = plot_settings["title"]
x_label = plot_settings["x_label"]
y_label = plot_settings["y_label"]
print(title + "-" + x_label + "-" + y_label)
# This is another way to concatenate strings that are in a list
print("-".join([plot_settings["title"],plot_settings["x_label"],plot_settings["y_label"]]))
#endregion

#region IF-Statement
# ---- If-Statement

# In python, an If-Statement is used to make decisions based on certain conditions. It allows the program to perform
# certain actions only when a certain condition is met. If the condition is not met, the program skips the actions 
# specified in the if-statement.

# The basic syntax for an if-statement is Python is as follows:
    
# if condition:
#       action1
# else:
#       action2

# The condition can be any expression that evaluates to either True or False. If the condition is True, then the
# program executes action1. If the condition is False, then the program executes action2.

# For example, suppose we want to print a message i a number is grater than 10. We can use if-statement to 
# accomplish this:

num = 8

if(num > 10):
    print("The number is grater than 10")
else:
    print("The number is not grater than 10")
    
# Indentation in python

x = 1 # this code is always executed
if x == 1:
    x += 1 # this code will be executed only within the if statement.
    
    test = 1 # this code will be executed only within the if statement.
# x = 0 # this code is always executed
#   x = 1 # this is wrong indentation

# nested if-statement

num = 9

if num > 10:
    if num < 20:
        print("The number is between 10 and 20")
    else:
        print("The number is grater than 20")
else: 
    print("The number is not grater than 10")

# In this example, first we test that a number is grater than 10, if it is,
# then we test if the number is less than 20. If both conditions are True, 
# we print the message "... number between 10 and 20", if number is not less
# than 20, we print a message indicating that the number id grater than 20.

# Lastly , we can also use logical operators (such as AND, OR and NOT) to 
# combine conditions in an if-statement.
# example:

num1 = -15
num2 = 10

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")

# The if statement can also be more complex with different combinations of
# the if, elif and else statement:
# Here is a breakdown of each statement:
    
# If: This statement is used to check if a particular condition is true. If 
# it is, then the code inside the if block is executed. If the condition is
# False, then the code is skipped.

# elif: This statement is used to check an additional condition if the 
# preceding if statement is False, then the code is skipped.

# else: This statement is used as a catch-all condition that is executed if
# all the preceding if and elif statements are false. If this is the case,
# then the code inside the else block is executed.

x = 4
if x < 5:
    print("x is less than 5")
elif x < 10:
    print("x is between 5 and 10")
else:
    print("x is greater than or equal to 10")
    
# In Python, you can use string comparison operators to compare strings in
# if statement. The following operators can be used to compare strings:

# == checks if two strings are equal
# != checks if two strings are not equal

fruit = "pinapple"
if fruit == "apple":
    print("This is an apple")
elif fruit == "banana":
    print("This is a banana")
else:
    print("This is not an apple or a banana")
    
# One more use for if statement is to check if a variable holds any value
# at all. E.g.: check if a filename was provided before trying to open it
# To do so, we can utilize the boolean abilities of specific data types:
    
# Strings
test_strings = ""
if not test_strings:
    print("String is empty") # output "String is empty
# The empty string is recognized as a boolean False

# Integers/Floats
test_number = 10
if test_number:
    print 
