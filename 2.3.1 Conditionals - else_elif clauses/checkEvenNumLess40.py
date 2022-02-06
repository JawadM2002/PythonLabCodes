# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates the use of if-else statements.
#              Checks if number is even and less than 40.
# ##

num = int(input("Enter an integer number: "))
if num % 2 == 0 and num < 40:
    print("Number entered is an even number and is < 40")
else:
    print("Number entered is an odd number or is < 40")

if num % 2 == 0 and num > 20:
    print("x is an even number and is > 20")
else:
    if num > 20:
        print("x is > 20.")
    else:
        print("x is an odd number.")