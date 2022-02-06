# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates the use of if-elif statements. Grade classification.
# ##

my_grade = int(input("Enter your grade: "))
if my_grade >= 70 :
    print("First")
elif my_grade >= 60:
    print("Upper second")
elif my_grade >= 50:
    print("Lower second")
elif my_grade >= 40:
    print("Third")
else:
    print("Fail")
