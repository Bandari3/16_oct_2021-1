# SYS

#import sys

# print(sys.path)
#
# sys.exit(1)
#
# print("After exit")

# stdin
# stdout
# stderr

# for data in sys.stdin:
#     if 'x' == data.rstrip():
#         break
#     print(f"Data: {data}")
#
# print("Exiting")

# sys.stdout.write("Python is awesome")

# OS

# import os
# from os import path
#
# print(os.getcwd())
#os.mkdir("test")
#os.chdir("test")
#print(os.getcwd())
#os.chdir("../")
#os.rmdir("test")
#os.remove("test123")
# print(os.environ)
# print(os.environ.get("PATH"))
#
# print(path.join(os.getcwd(), "builtins.py"))
# print(path.exists("testdir"))
# print(path.isfile("testdir"))
# print(path.isdir("builtins.py"))
# print(path.abspath('.'))
# print(path.normpath('C:\\Users\\tewar\\projects\\16_oct_2021\\Module3'))
# print(path.split('C:\\Users\\tewar\\projects\\16_oct_2021\\Module3\\builtins.py'))

# Subprocess
# import subprocess
#
# subprocess.call(["C:\\Program Files (x86)\\TuxPaint\\tuxpaint.exe"])
#
# output = subprocess.check_output(["ls", "-l"])
#
# from subprocess import Popen, PIPE
#
# process = Popen(["echo", "Hello"], stdout=PIPE, stderr=PIPE)
#
# stdout, stderr = process.communicate()

# MATH

# import math
#
# print(math.log(6, 2))

# Random

# import random
#
# print(random.random())
# print(random.randint(1, 999))
#
# print(random.randrange(0, 1000, 5))

# Datetime

# import datetime
#
print(f"Current date time: {datetime.datetime.now()}")

print(f"Current date time: {datetime.datetime.now().strftime('%d-%m-%y %H:%M')}")

print(datetime.date.today().strftime("%Y"))
print(datetime.date.today().strftime("%B"))
print(datetime.date.today().strftime("%W"))

from datetime import datetime, timedelta

one_month_from_now = datetime.now() + timedelta(days=30)
print(one_month_from_now)
print(datetime.now() + timedelta(days=500))

# Zipfile

import zipfile

zf = zipfile.ZipFile("module3", "w")
zf.write("builtins.py")
zf.write("functions.py")
zf.close()

zf = zipfile.ZipFile("module3.zip", "r")
zf.extract("builtins.py")
zf.close()
print(zipfile.is_zipfile("module3.zip"))
print(zipfile.is_zipfile("builtins.py"))