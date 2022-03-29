import random
import sys
import math
import threading
import time
from functools import reduce


# If Else Statment
var = 25

if var > 21:
    print("Y")
elif var >= 16:
    print("N")
else:
    print("Negative")


# Condintion true if condintion else condintion is false
aBoolean = True

aBoolean = True if var >= 25 else False
print(aBoolean)

# Checking the first 4 characters in the string 
str_1 = "Strings"
print("1st chars to 4 \n\n", str_1[0:4])

# Checking for the word is "is" in the string str_1 will print false to the console
print("is" is str_1)


print(r"Ignored")

someRandomString = "StringsAreCool"
print("1st 3", someRandomString[0:3])
print("Every other chararcter" ,someRandomString[0:-1:2])
someRandomString = someRandomString.replace("StringsAreCool", "StringsAreSuperCool")
print(someRandomString)


someRandomString = someRandomString[:8] + "R" + someRandomString[9:]
print(someRandomString)

print("?" not in someRandomString)

print("You index", someRandomString.find(">>"))

print("        Hello      ".rstrip())


print("  ".join(["Some", "Letters"]))

print("A letters".split(" "))

int1 = int2 = 5
print(f'{int1}+{int2} = {int1 + int2}')

