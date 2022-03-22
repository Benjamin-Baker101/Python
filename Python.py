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


