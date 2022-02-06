# This program calculates the time it takes, in minutes, for two water hoses to fill a pool
# given the time, in hours, each hose separately takes to fill the same pool.
# #### version 2 - less verbose but still readable! ####

# Time taken to fill pool in hours
timeGreen = 1.5
timeRed  = 1.2

# Rate each hose takes to fill the pool in minutes.
rateHoseGreen = 1 / (60 * timeGreen)
rateHoseRed = 1 / (60 * timeRed)

# Time it takes to fill pool using both hoses in minutes
timeToFillPool = 1 / (rateHoseGreen + rateHoseRed)
print(timeToFillPool)