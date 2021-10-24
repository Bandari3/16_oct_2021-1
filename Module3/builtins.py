# Builtins

# # sorting
#
# list_of_nums = [45, 32, 90, 100, 1, 15]
#
# print(sorted(list_of_nums, reverse=True))
# list_of_nums.sort()
# print(list_of_nums)
#
# # Sorting on index
#
# friends_with_age = [("Samar", 67), ("Priya", 29), ("Sam", 32), ("Simran", 45), ('Parul', 45)]
#
# from operator import itemgetter
# print(sorted(friends_with_age, key=itemgetter(1, 0)))

# Lambda
#
# def sum(x, y):
#     return x + y

#sum = lambda x, y: x + y

#print((lambda x, y: x + y)(10, 16))
#
# def table(n):
#     return lambda a:a*n
#
# n = int(input("Enter a number: "))
#
# b = table(n)
#
# for i in range(1, 11):
#     print(f"{n} X {i} = {b(i)}")

# lambda with filter

list_of_nums = [1, 2,3,4,5,6,7,8,9,10]
oddlist = list(filter(lambda x:(x%2!=0), list_of_nums))
print(oddlist)

# map

squares = list(map(lambda x: x**2, list_of_nums))
print(squares)

print(dir(squares))

import functions

from functions import *

students(name="Dimple", age=23)

