# try:
#     x = int(input("Enter a number to add: "))
#     y = int(input("Enter a number to add: "))
#     print(f"{x} + {y} = {x+ y}")
# except ValueError:
#     print("Invalid input, please enter a number")

#
# try:
#     x = int(input("Enter a number to divide: "))
#     y = int(input("Enter a number to divide: "))
#     print(f"{x} / {y} = {x / y}")
# except ValueError:
#     print("Invalid input, please enter a number")
# except ZeroDivisionError:
#     print("Cannot divide number by zero")
# except Exception as err:
#     print(f"Cannot divide, exception occurred: {str(err)}")
# else:
#     print("Program executed successfully")
# finally:
#     print("Program ended")


# try:
#     file = open("test.txt", "r")
#     file.read()
# except Exception as err:
#     print(f"Cannot write to the file: {str(err)}")
# finally:
#     file.close()

#
# try:
#     x = int(input("Enter a number to divide: "))
#     y = int(input("Enter a number to divide: "))
#     print(f"{x} / {y} = {x / y}")
# except (ValueError, ZeroDivisionError):
#     print("Invalid input, please enter a number greater than zero")
# except Exception as err:
#     print(f"Cannot divide, exception occurred: {str(err)}")
# else:
#     print("Program executed successfully")
# finally:
#     print("Program ended")


# Assert Statements


def average_marks(marks):
    try:
        assert len(marks) != 0
        return sum(marks)/len(marks)
    except AssertionError:
        return "No Marks passed"

marks = []
print(average_marks(marks))