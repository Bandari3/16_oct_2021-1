# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Student admission completed")
#
#
# ram = Student("Ram", 23)
# print(ram.name)
# print(ram.age)
# Inheritance
# Polymorphism
# Data Abstraction
# Encapsulation

# Inheritance

# class Animals:
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("Animals Speaking")
#
#
# class Dog(Animals):
#     def bark(self):
#         print("Dog Barking")
#
#
# d = Dog(name="Scooby")
# d.speak()
# d.bark()
# print(d.name)

# Multi Level Inheritance

# class Animals:
#
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("Animals Speaking")
#
#
# class Dog(Animals):
#     def bark(self):
#         print("Dog Barking")
#
#
# class Pup(Dog):
#
#     def eat(self):
#         print("Puppy eats")
#
#
# d = Pup(name="Scooby")
# d.speak()
# d.bark()
# d.eat()
# print(d.name)

# Multiple Inheritance

class Sum:
    def summation(self, a, b):
        return a+b
    def multiplication(self, a, b):
        return "Multiply"

class Multiply:
    def multiplication(self, a, b):
        return a*b
    def summation(self, a, b):
        return "sum"

class Calculator(Multiply, Sum):
    def division(self, a, b):
        return a/b

    def subtract(self, a, b):
        return a-b

calc = Calculator()

print(calc.summation(7, 8))
print(calc.multiplication(7, 8))
print(calc.division(8, 4))
print(calc.summation(10, 9))

# MRO: Method Resolution Order