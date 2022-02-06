# Allows a list an unlimited number of names to be entered into an employees list and then displayed.

# Create abd Initialise employees list to an empty list.
# If employees is not initialised, an error will be thrown on line 12.
employees = []
# Initialise the variable name to hold the employee names entered.
name = input('Please enter a name: ')

# Use a while loop to get all the names we need. A while loop is used because we don't know the number of names needed.
# The loop will terminate when the name entered is equal to 'end' and the spec for exercise 5 asked.
while name != 'end':
    employees.append(name)
    name = input('Please enter a name: ')

# Display the list of employee names.
print(employees)

# Note: to make your code more robust, you must check if employees is not empty
# if not employees:
#     print("The employee list is empty!!")
# else:
#     print(employees)
