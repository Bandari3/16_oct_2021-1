
# Hello i am a comment
print("hello")


"""
Hello
i
am
a 
comment
"""

# Integers

var1 = 20
var2 = 10

print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1/var2)
print(var2 % var1)
print(var1**2)

print(var1//var2)
print(9//5)
print(type(3+4j))
print(hex(9))

print(5 < 2)
print(5 > 2)
print(5 == 2)
print(5 != 2)
print(5 <= 2)
print(5 >= 2)

# Bitwise Operation
"""
# AND
 0 & 0 = 0
 0 & 1 = 0
 1 & 0 = 0
 1 & 1 = 1


# OR
 0 | 0 = 0
 0 | 1 = 1
 1 | 0 = 1
 1 | 1 = 1

# XOR
 0 ^ 0 = 0
 0 ^ 1 = 1
 1 ^ 0 = 1
 1 ^ 1 = 0
"""

print(bin(7))
print(bin(5))
print(int('010', 2))
print(7 | 5)
print(7 & 5)
print(7 ^ 5)
print(7<<5)
print(int('11100000', 2))
print(7>>5)


# String

name = "Saurabh"
age = "10"
print(type(age))
print(type(name))
# Concatenation
print(name +  ' ' + age)
# Repetition

print(name * 3)

# Indexing and Slicing
print(name[3])
print(name[0:3])
print(name[-1])
print(name[-4:-1])
print(name[-4:])
print(name[:4])

print(name[::-1])

# Membership Checking
greeting = "Hello there, how are you"
print('how' in greeting)
print('how2121' not in greeting)
print('how' not in greeting)
print(len(name))

# String formatting
name = "Priya"
age = 39
print("Hello {name}. You are {age} years old".format(age=age, name=name))
#
# # F-string
print(f"Hello {name}, you are {age} years old")

# String functions

name = "Priya"
print(name.capitalize())
print(name.upper())
print(name.lower())

account_num = '10'
print(account_num.zfill(16))

print(name.find('z'))

string = "python is awesome"
print(string.islower())
print(string.isupper())
print(name.isalpha())
#print(string.index('zz'))
print(string.count('o'))
print(string.replace('awesome', 'great'))
print(string.split('o'))

# Indentation

if "is" in string:
    print("hello there")