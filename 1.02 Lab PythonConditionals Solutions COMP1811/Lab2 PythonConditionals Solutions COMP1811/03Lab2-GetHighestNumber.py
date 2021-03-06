# Finds the greatest of three numbers entered by the user

# Get three numbers from user:
int1 = int(input("Enter your first number: "))
int2 = int(input("Enter your second number: "))
int3 = int(input("Enter your third number: "))

# Solution 1
if (int1 >= int2) and (int1 >= int3):
    highestNum = int1
elif (int2 >= int1) and (int2 >= int3):
    highestNum = int2
else:
    highestNum = int3
print("Sol1 - The highest number is:", highestNum)

# Solution 2
highestNum = int1 if (int1 >= int2 and int1 >= int3) else int2 if (int2 >= int1 and int2 >= int3) else int3
print("Sol2 - The highest number is:", highestNum)
