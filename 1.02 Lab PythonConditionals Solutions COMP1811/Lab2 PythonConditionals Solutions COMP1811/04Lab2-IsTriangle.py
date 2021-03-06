#COMP1811 - Exercise 4.1 possible solutions
#Determines whether 3 input triangle side lengths form a triangle
#The solution is based on the Triangle Inequality Theorem, which states that
# the sum of two side lengths of a triangle is always greater than the third side.
#Four alternative solutions are provided

#Input from the user
x = int(input("Please enter 1st triangle side length: "))
y = int(input("now enter the 2nd side length: "))
z = int(input("and lastly the 3rd: "))

#The Triangle Inequality Theorem
#Solution 1
if x+y>z and x+z>y and y+z>x:
    print("Sol1: It's a triangle, yay!")
else:
    print("Sol1: It's not a triangle!")

#Solution 2
# Uses syntactic sugar to for the "if" statement
# i.e. the code is written on one line - as a simple equation is needed
print("Sol2: It's a triangle, yay!") if (x+y>z and x+z>y and y+z>x) else print("Sol2: It's not a triangle!")

#Solution 3
# Uses the same syntactic sugar but assigns a resulting Boolean value to isTriangle
# This method is useful if you intend to use the result later in your program or for use with functions
isTriangle = True if (x+y>z and x+z>y and y+z>x) else False
if isTriangle:
    print("Sol3: It's a triangle, yay!")
else:
    print("Sol3: It's not a triangle!")


#COMP1811 - Exercise 4.2
if (x+b == c) or (x+c == b) or (b+c == x):
    print("The triangle is degenerate.")