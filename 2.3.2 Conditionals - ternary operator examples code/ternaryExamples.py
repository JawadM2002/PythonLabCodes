# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates the use of the ternary operator and shows the equivalent code using multiline conditionals.
# ##

a = 20
b = 47
# get smallest of two values
smallest = a if a < b else b
print("The smallest value is:", smallest)
smallest = "a" if a < b else "b"
print(smallest, "is the variable with the smallest value.")

# The code block above is equivalent  to the following:
if a < b:
    smallest = a
else:
    smallest = b
print("The smallest value is:", smallest)

# is x odd?
x = 10
is_odd = True if x%2 != 0 else False
print("is",x, "odd ?", is_odd)

# The code block above is equivalent  to the following:
if x%2 != 0:
   is_odd = True
else:
   is_odd = False
print("is",x, "odd ?", is_odd)

# is grade a pass?
grade = 56
pass_status = "pass" if grade >= 40 else "fail"
print("Your grade", grade, "is a", pass_status)

# The code block above is equivalent  to the following:
if grade >= 40:
    pass_status = "pass"
else:
    pass_status = "fail"
print("Your grade", grade, "is a", pass_status)

# Get age category
age = 25
age_category = 'Child' if age < 13 else 'Teenager' if age < 18 else 'Adult'
print("Age category is:", age_category)

# The code block above is equivalent  to the following:
if age < 13:
  age_category = 'Child'
elif age < 18:
  age_category = 'Teenager'
else:
  age_category = 'Adult'
print("Age category is:", age_category)

# shares action
shares = 100
print('hold') if shares==0 else print('sell') if shares<0 else print('buy')

# The code block above is equivalent  to the following:
if shares != 0:
    if shares < 0:
        print('sell')
    else:
        print('buy')
else:
   print('hold')

# The code block above is equivalent  to the following:
if shares == 0:
   print('hold')
elif shares < 0:
   print('sell')
else:
   print('buy')

# The following are legal in Python
x = 10
y = 3
if x!=5: x+=y; print(x); print(y)
x=5; y=8; z=y*x; print(z)


