
file = open("test.txt", 'r')
if file:
    print("File is opened successfully")
data = file.read(10)
print(data)
print(type(data))
print(file.read(10))
file.close()

file = open("test.txt", 'r')
if file:
    print("File is opened successfully")
data = file.readline()
print(data)
data = file.readline()
print(data)
file.close()

file = open("test.txt", 'r')
if file:
    print("File is opened successfully")
data = file.readlines()
for line in data:
    print(line)

file.close()

file = open("test.txt", 'r')
if file:
    print("File is opened successfully")
for line in file:
    print(line)

file.close()

# Writing to a file

file = open("test.txt", 'w')
if file:
    print("File is opened successfully")
file.write("Python is Awesome, I love coding in Python")

file.close()

file = open("test.txt", 'a')
if file:
    print("File is opened successfully")
file.write("\nPython is Awesome, I love coding in Python")

file.close()

# With Statement

with open("test.txt", "a+") as file:
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.read())
    print(file.tell())

print(file.closed)


