import os

os.getcwd()
os.mkdir("demo")

# FILESTREAM ------------------------
# mode w
f = open("demo/new_file.txt", "w")
f.write("hello this is the first line\n")
f.write("end of the file\n")
f.close()

with open("demo/with_file.txt", "w") as f:
    f.write("2nd attemp on the filestream\n")
    f.write("random words\n")

# mode a
f = open("demo/with_file.txt", "a")
f.write("this is the 3rd line")
f.write("4th line")
f.close()

# mode r
filename = "demo/with_file.txt"
f = open(filename, "r")
f.read()
f.read()
f.close()

f.readline()
f.readlines()

# array
f = open(filename, "r")
lines = f.readlines()
f.close()

print("This is %s" % filename)
for line in lines:
    print("- ", line)

# REGULAR EXPRESSION ------------------------
import re

re.findall()

string = "ab34ca777_888_222_jijoe8ilkn3#$alj_%"

# we want to extract 777, 222, and 888
# + 1 or more
# * 0 or more
# ? 0 or 1
re.findall(r"\d", string)

# greedy search
re.findall(r"\d+", string)
# non-greedy search
re.findall(r"\d+?", string)

# \d: numeric digits: [0-9]
# \w: alphanumeric: [a-z A-Z 0-9]
# mixed with alphabets
re.findall(r"\w{2}\d{2}", string)
re.findall(r"\d{1}[a-z]{3}", string)
