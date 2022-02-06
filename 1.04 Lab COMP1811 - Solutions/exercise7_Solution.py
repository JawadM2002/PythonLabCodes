# Calculates the factorial of integer entered.

# Initialise x to the number entered.
x = int(input("Pleae enter a positive integer:"))

if x == 0:
    factorial = 1
elif x < 0:
    factorial = "factorials don't exist for negative numbers!"
else:
    # Initialise factorial to 1 because factorial of 0 and 1 is 1.
    factorial = 1
    # Calculate factorial by repeatedly multiplying the current factorial by current x. Decrement x on each iteration.
    while x > 0:          # Terminate loop when control variable x is 0.
        factorial *= x
        x -= 1            # Decrement number to change control variable x.

print("Factorial of the integer is:", factorial)
