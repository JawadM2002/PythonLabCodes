# COMP1811 Lab3 - Exercise 5 possible solution
# The program determines whether or not theme park goers can go on available rides at the Magic Kingdom theme park.
#
# There are many ways to improve the code for example by using dictionaries and a switcher structure
# revisit the code when these topics have been covered.
# The code considers good HCI practice and does not ask user to input info that is not necessary for the ride selected
#


# Display available rides and get user's choice
print("""1 Carnival Carousel
2 Dodgems
3 Pandemonium
4 Phantom Ghost Zone
5 Scenic River Cruise""")
rideNum = int(input("Select a ride and enter its number here: "))

# Check ride number entered is between 1 and 5
if not(1 <= rideNum <= 5):    # there are other ways of checking range and we'll cover those later on the module
    print("You've entered a ride number that does not exist! Please try again.")
# Check ride restrictions
elif rideNum == 5:
    print("You've selected to go on the Scenic River Cruise.")
    print("""There are no age or height restrictions for this ride, 
                  welcome aboard...""")
else:
    age = int(input("Please enter your age: "))
    if rideNum == 1:
        print("You've selected to go on the Carnival Carousel ")
        print("and you're all OK to go.") if age >= 5 else print("but you're too young to go on this ride, sorry!")
    elif rideNum == 4:
        print("You've selected to go on the Phantom Ghost Zone ")
        print("and you're at the right age to go on this ride.") if age >= 8 else print("but you're too young!")
    else:
        height = int(input("Please enter your height in centimeters: "))
        if rideNum == 2:
            print("You've selected to go on Dodgems ")
            # Note that as the following line is too long, it is split just after a parenthesis
            # This is the preferred way of wrapping long lines is by using Python's
            # implied line continuation inside parentheses
            print("and you're all OK to go.") if age >= 12 and height >= 130 else print(
                "but you don't meet the restrictions to go on this ride, sorry!")
        elif rideNum == 3:
            print("You've selected to go on Pandemonium ")
            print("and its fine for you to go on the ride.") if 16 <= age <= 70 and 140 <= height <= 200 else print(
                "but you don't meet the restrictions to go on this ride, sorry!")


