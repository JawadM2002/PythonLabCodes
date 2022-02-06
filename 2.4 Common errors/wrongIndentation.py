# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates syntax and logical errors caused by wrong indentation.
#              Try to fix those errors..
# ##

# if x is even divide by 2,
# otherwise, add 1 before dividing by 2.
# The following lines of code cause syntax error, try to fix it.
if x%2==0:
   x /= 2
print(x)
else:
   x = (x+1)/2
   print(x)

# The following lines of code cause logical error, try to fix it.
if x%2==0:
   x /= 2
   print(x)
else:
   x = (x+1)/2
print(x)

# The following lines of code contain syntax error. Try to fix it.
if x%2==0:
   x /= 2
   print(x)
   else:
     x = (x+1)/2
     print(x)

