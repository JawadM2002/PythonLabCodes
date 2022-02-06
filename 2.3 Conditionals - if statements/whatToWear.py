# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates the use of if statements. Suggests what to wear.
# ##

wet = True
cold = False

#
if wet:
    print("Wear a waterproof coat, and \nmaybe take an umbrella.") # Note tha \n is an escape sequence for new line.
                                                                   # \n forces a carradge return and the text will be
                                                                   # displayed on next line
if not wet:
    print("No need to wear a waterproof coat or take an umbrella.")
if cold:
    print("Wear a warm coat.")
if not cold:
    print("A jacket will be enough.")


# Final note: there is a better way to write this programe by using if-else statements-
# see whatToWear1.py
