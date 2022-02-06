# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 3.0
# Description: Demonstrates the use of nested if-else statements. Suggests what to wear.
# ##

cold = True
wet = True
if wet:
    if cold:
        print("Wear a waterproof coat.")
    else:
       print("Take an umbrella.")
else:
    if cold:
        print("Wear a warm coat.")
    else:
        print("A jacket is enough.")
