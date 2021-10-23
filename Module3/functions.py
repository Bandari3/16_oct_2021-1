# Creating a function

# def greet():
#     print("Hello there, How are you doing")
#
# greet()

# Parameters to a Functions

# def greet(name):
#     print(f"Hello {name}, How are you doing")
#
#
# name = input("Enter your name: ")
# greet(name)

# def get_values():
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     return x, y
#
# def chk_division(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False
#
# x, y = get_values()
#
# if chk_division(x, y):
#     print(f"{x} is divisible by {y}")
# else:
#     print(f"{x} is not divisible by {y}")


# Python call by reference and value

# def update_str(string):
#     print(f"Value inside function before update: {string}")
#     print(hex(id(string)))
#     string = "new string"
#     print(hex(id(string)))
#     print(f"Value inside function: {string}")
#
# string = "actual string"
# update_str(string)
# print(hex(id(string)))
# print(f"Outside function: {string}")


# def update_list(new_list):
#     print(f"Value inside function before update: {new_list}")
#     print(hex(id(new_list)))
#     new_list.append("Test")
#     print(hex(id(new_list)))
#     print(f"Value inside function: {new_list}")
#
# new_list = ["abc", "def", "xyz"]
# update_list(new_list)
# print(hex(id(new_list)))
# print(f"Outside function: {new_list}")

# Types of Arguments
# 1. Required Arguments or Positional Arguments

def division(x, y):
    print(f"x= {x}")
    print(f"y= {y}")
    return x / y

print(division(2, 5))

# Keyword Argument

# def division(x, y):
#     print(f"x= {x}")
#     print(f"y= {y}")
#     return x / y
#
# print(division(y=2, x=5))
#
# def simple_interest(p,t,r):
#     return (p*t*r)/100
#
# print(f"Simple interest: {simple_interest(t=10, r=5, p=100000)}")

# Default Arguments

# def simple_interest(p,t,r=8):
#     return (p*t*r)/100
#
# print(f"Simple interest: {simple_interest(t=10, p=100000)}")


# Variable length or Arbitrary Arguments

# def sum(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum
#
# print(sum(3, 4))
# print(sum(3, 4, 5))
# print(sum(3, 4, 6, 5))
# print(sum(3, 4, 6, 5, 7))
# print(sum(3, 4, 6, 5, 7, 8))
# print(sum(3, 4, 6, 5, 7, 8, 9, 10, 11, 12))
#
# # Arbitrary Keyword Arguments
#
def students(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

students(name="Saurabh", age=32, subject="CSE", location="Delhi", GPE=7.9)


# Scope of a variable

# 1. Local Variable
# 2. Global Variable

value = 6789
def print_value():
    global value
    value = 12345
    print(value)
print_value()
print(value)

