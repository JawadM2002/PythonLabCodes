# This program calculates the time it takes, in minutes, for two water hoses to fill a pool
# given the time, in hours, each hose separately takes to fill the same pool.
# #### version 3 - much less lines of code and perhaps less readable! ####

# Time taken to fill pool in hours
timeGreen = 1.5
timeRed  = 1.2

# Time it takes to fill pool using both hoses in minutes
print(1 / ((1 / (60 * timeGreen)) + (1 / (60 * timeRed))))
