from ast import arg
from calendar import different_locale
from genericpath import exists
import random
import re
from statistics import mode
import sys
import math
import threading
import time
from functools import reduce
from typing import List
from webbrowser import get


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

l1 = [1, 2.23, "Ben,  True"]
print("The Length", len(l1))
print("1st", l1[0])
print("Last", l1[-1])


l1[0] = 2
l1[2:4] = ["John", False]
l1[2:2] = ["Jim", 13]
l1.insert(1, 3.14)
l2 =  l1 + ["Multimeter" , 4]
print("l2" , l2)

l2 = ["Electricity, 4"] + l1

l3 = [[1, 2], [3,4]]
print("[1,1]", l3[1][1])

print("1 exists", (1 in l3))
print("Min", min([1,2,3]))
print("Max", max([1,2,3]))
print("1st 2", l1[0:2])
print("Every Other", l1[0:-1:2])
print("Reverse", l1[::-1])

# While Loops

while_1 = 0

while while_1 < 5:
    print(while_1)
    while_1 = while_1 + 1
    

while_2 = 0
while while_2 <= 20:
    if while_2 % 2 == 0:
        print(while_2)
    elif while_2 == 9:
        break
    else:
        while_2 = while_2 + 1
        continue
    while_2 = while_2 + 1


l4 = [1,3,5,7.76, "Yards"]

while len(l4): 
    print(l4.pop(0))



# For Loops

for x in range(0, 11):
    print(x, ' ', end="")
    print()

l5 = [1,7.76, "Yards"]
for x in l5:
    print(x)

for x in [2,4,6]:
    print(x)


# Iterators

l6 = [18,20,22]
itr = iter(l6)
print(next(itr))

# Ranges
print(list(range(0,10,2)))

num_list = [[1,2,3], [4,5,6], [7,8,9]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


# Tuples

t1 = (1,3.14,"Chris")
#print("Length",len(0))
print("1st  ",t1[0])
print("Last",t1[-1])
print("1st 2", t1[0:2])
print("Every Other", t1[0:-1:2])
print("Reverse",t1[::-1])


# Dictionaries

units = {
    "Kph":"Mph",
    "PSI":"Pascals"

}

electricity = dict({

    ("MilliVolts", "Amps"),
    ("Volts", "Watts")

})


print("Length", len(units))
print(units["Kph"])
units["Knots"] = "VerticalSpeed"
print(list(units.items()))
print(list(units.values()))
print(list(units.keys()))


del units["Kph"]
print(units.pop("PSI"))
print("Psi" in units)

for k in units:
    print(k)


for v in units.values():
    print(v)


d1 = {"Name" : "Electronics", "Price" : 345.24}
print("%(Name)s Cost $ %(Price).2f" % d1)

# Sets

s1 = set(["Purple", 1])
s2 = {"Yellow", 1}
print("Length", len(s2))
s3 = s1 | s2
print(s3)
s3.add("Blue")
s3.discard("Purple")
print("Random", s3.pop())
s3 |= s2
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
s3.clear()
s4 = frozenset(["Orange", 7])


# Functions

def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2

print(get_sum(5,23))



def get_sum2(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum
print(get_sum2(1, 3 ,5 ,7))


def next_2(num):
    return num + 1, num + 2

i1, i2 = next_2(9)
print(i1, i2)

def mult_by(num):
    return lambda x: x * num
print("3 * 5 =", (mult_by(3)(5)))

def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)


power_list = [lambda x: x**2,
              lambda x: x**3,]

#Maps

one_to_4 = range(1,5)
times_2 = lambda x: x * 2
print("List:  ", list(map(times_2, one_to_4)))

print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

print(reduce((lambda x,y: x + y), range(1,6)))

# Exception Handling

# while True:
#     try:
#         number = int(input("Enter A Number"))
#         break
#     except ValueError:
#         print("You didnt enter a number")
#     except:
#         print("Unknown Error")
# print("Correct")


# File I/O

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Text \nRandom \nStuff")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)

# Classes And Objects

class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Enter Numbers Only For Height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width
        
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Enter Numbers Only For width")

    

    def get_area(self):
        return int(self.__width) * int(self.__height)

square = Square()
square.height = "10"
square.width = "10"
print("Area", square.get_area())


# Inheritance & Polymorphism

class Animal:
    def __init__(self, name="unknown", height=0):
        self.__name = name
        self.__height = height
    
    @property
    def name(self, name):
        self.__name = name

    def roaring_noise(self):
        return "Rarwaararrr!!"
    
    def __str__(self):
        return "{} is a {} and says {}".format(self.__name, type(self).__name__)