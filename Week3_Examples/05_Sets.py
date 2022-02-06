"""
    This program shows how SETs are used.
"""
# Create two sets.
class_list = {'Ted', 'Doris', 'Daisy', 'Theo', 'Les'}
attended = {'Doris', 'Theo', 'Les'}
print(attended)  # Print the items in a set.

# An item only appears once in a set.
attended.add('Doris')  # Trying to add a second Doris.
print(attended)        # But there is still only one.

# Add and remove items from a set.
attended.remove('Theo')
attended.add('Clara')
print(attended)

# We can use sets as in mathematics.
missing = class_list - attended
print(missing)
