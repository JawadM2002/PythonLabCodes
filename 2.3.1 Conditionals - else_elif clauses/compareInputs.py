# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates the use of if-elif statements. Compares input values.
# ##

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))

# Using an else clause
if x < y :
    print("x is less than y.")
elif x > y:
    print("x is greater than y.")
else:
    print("x is equal than y.")

# Same code without the else clause
if x < y :
    print("x is less than y.")
elif x > y:
    print("x is greater than y.")
elif x == y:
    print("x is equal than y.")