# Allows a list of five names to be entered into an employees list and then displayed.

# Initialise employees list to an empty list. If employees is not initialised, an error will be thrown on line 10.
employees = []

# Use a for loop to get all the 5 names we need. A for loop is used because we know the number of names needed.
for i in range(5):
    employees.append(input('Please enter a name: '))

# Display the list of employee names.
print(employees)
