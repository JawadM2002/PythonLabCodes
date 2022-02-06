"""
    This program sets up the LISTs of departments
    which is then amended and a list of floats.

"""
first = ['Sales', 'Production', 'Accounts']
print(first)   # Print the whole list.

# This adds the Research department to the list.
first.append('Research')
print(first)   # This shows the amended list.

# Let's change the first department to Joke.
first[0] = 'Joke'   # Numbering starts at 0!
print(first)

# This creates a list of floats.
third = list(range(0, 101, 10))
the_floats = list()
for item in third:
    the_floats.append(item / 100)
print(the_floats)
