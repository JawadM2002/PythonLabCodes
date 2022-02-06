# ######################################################
# Author: Yasmine Arafa
# Date Created: 01/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Code from the lecture notes on Data Types
# ######################################################

# To find out a variables data type use the function type()
type(1)       # int
type("Hello") # str
x = 10.5
type(x)       # float

# Dynamic typing
x = 4
x = "four"
x = 4.0
type(x)
x = 100 / 3
print(x)
x = 100.0 / 3.0
print(x)

# The following code contains errors, can you fix it?
x = 4 + "four"
x = 4 + "4.0"
x = 4 + float("4.0")

# Converting types
x = float(9)
print("x's type is ", type(x))

x = int(5.3)
print("x's type is ", type(x))

x = float("10")
print("x's type is ", type(x))

x = int("10")
print("x's type is ", type(x))

x = int("six")
print("x's type is ", type(x))

x = str(9.3)
print("x's type is ", type(x))

x = float("5.2")
print("x's type is ", type(x))

x = int("10.6")
print("x's type is ", type(x))

x = float("ten")
print("x's type is ", type(x))