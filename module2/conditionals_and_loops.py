# Conditionals

# if else

# number = int(input("Enter a number: "))
# number2 = int(input("Enter another number: "))

# if number > number2:
#     print(f"{number} is greater than {number2}")
# else:
#     print(f"{number2} is greater than {number}")

# if number > number2:
#     print(f"{number} is greater than {number2}")
# elif number == number2:
#     print("Both numbers are equal")
# else:
#     print(f"{number2} is greater than {number}")

# Structural pattern matching
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# match age:
#     case 18:
#         print("You are 18 years old")
#     case 20:
#         print("You are 10 years old")
#     case 10:
#         print("You are 10 years old")

# While
# i = 1
# while i <= 10:
#     print(f"{i}**2 is: {i**2}")
#     i += 1


# name = "Peter"
# guess = input("Guess the person name that is in my mind: ")
# pos = 0
#
# while guess != name and pos < len(name):
#     print(f"Incorrect guess. Hint letter: {pos+1} is {name[pos]}.", end='')
#     guess = input("Try again: ")
#     pos += 1
#
# if pos == len(name) and name != guess:
#     print(f"You were not able to guess the name. The name was {name}")
# else:
#     print(f"\nGreat, you got in {pos+1}th attempt")

# While loop with else


# i = 1
# while i <= 10:
#     print(f"{i}**2 is: {i**2}")
#     i += 1
# else:
#     print('Loop ended')

# For
# limit = int(input("Enter a range to find prime numbers: "))
#
# for n in range(2, limit+1):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x}*{n//x}")
#             break
#     else:
#         print(f"{n} is a prime number")


# friends = ["Sam", "Peter", "Priya"]
# for f in friends:
#     if f == "Peter":
#         break
#     print(f)
# print("Loop ended")


friends = ["Sam", "Peter", "Priya"]
for f in friends:
    if f == "Peter":
        continue
    print(f)
print("Loop ended")