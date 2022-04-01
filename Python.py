import random
import sys
import math
import threading
import time
from functools import reduce
from typing import List


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

# Strings
str_1 = "Strings"
print("1st CHARS to 4 \n\n", str_1[0:4])


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

print("You index", someRandomString.find("A"))

print("        Hello      ".rstrip())


print("  ".join(["Some", "Letters"]))

print("A letters".split(" "))

int1 = int2 = 5
print(f'{int1}+{int2} = {int1 + int2}')


print("A SMALL STRING".lower())
print("A Big String".upper())

print("ABig String".isalnum())
print("IsAlpha".isalpha())
print("124".isdigit())


# Lists 

li = [1,2.23,"Ben, True"]
print("The Length", len(li))
print("1st", li[0])
print("Last", li[-1])


li[0] = 2
li[2:4] = ["John", False]
li[2:2] = ["Jim", 13]
li.insert(1, 3.14)
l2 =  li + ["Multimeter" , 4]
print("l2" + l2)
