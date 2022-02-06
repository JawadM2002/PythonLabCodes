# ##
# Author: Yasmine Arafa
# Date Created: 02/09/20
# Date Updated: no updates
# Version: 1.0
# Description: Demonstrates if statements with a guessing game.
# ##

import  random

# Get random number between 1 and 10
random_num = random.randint(1,10)
# Get user to guess a number
input_num = int(input("Guess a number between 1 and 10: "))

# Check if number entered is equal to the generated random number
if input_num == random_num:
    print("It’s a match. You win!")

# Check if number entered is greater than the generated random number
if input_num > random_num:
    print("Too high! try again...")

# Check if number entered is less than the generated random number
if input_num < random_num:
    print("Too low! try again...")

# Final note: there is a better way to write this programe by using if-else statements-
# see numGuessingGame1.py
