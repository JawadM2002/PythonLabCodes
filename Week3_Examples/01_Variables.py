"""
    This program shows how variables are used.
"""
name = 'Andy'   # String
age = 87        # Integer
sane = False    # Boolean
height = 1.83   # Float

print(name)
print('Andy is', f'{age * 365: ,} days old.')
print(name, 'is sane.') if sane else print(name, 'is mad.')
print(name, 'is', height * 100, 'centimeters tall.')
