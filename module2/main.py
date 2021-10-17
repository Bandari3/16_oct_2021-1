# Reserved Keywords

#if = "hello there" -- Wont work

import keyword
#
print(keyword.kwlist)

# Command line arguments

import sys

print(f"Number of arguments: {len(sys.argv) -1 }")
print(f"Argument list: {str(sys.argv[1:])}")

name = sys.argv[1]
age = sys.argv[2]
print(f"Hello {name}, you are {age} years old")


# User input

name = input("Enter your name: ")
age = int(input("Enter you age: "))
print(type(age))
print(type(name))
print(f"Hello {name}, you are {age} years old")
print(f"Age in months: {age * 12}")