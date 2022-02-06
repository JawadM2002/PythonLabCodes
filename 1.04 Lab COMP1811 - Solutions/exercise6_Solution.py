# Creates an employees dictionaru with there extension numbers and displays the extension of an employee name entered.

# Create abd Initialise employees dictionary to an empty dictionary
# If employees is not initialised, an error will be thrown on line 10.
employees = {}
# Initialise the variable name to hold the employee names entered.
name = input('Please enter a name: ')

# Use a while loop to get all the names we need. A while loop is used because we don't know the number of names needed.
# The loop will terminate when the name entered is equal to 'end' and the spec for exercise 5 asked.
while name != 'end':
    employees[name] = input('Please enter their extension: ')
    name = input('Please enter a name: ')

# Display the name and extension of an employee.
name = input('Enter the employee name whose extension you need:')
print('The extension for ' + name + ' is ' + employees[name])

