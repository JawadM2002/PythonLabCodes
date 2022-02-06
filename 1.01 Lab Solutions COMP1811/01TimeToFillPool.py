# This program calculates the time it takes, in minutes, for two water hoses to fill a pool
# given the time, in hours, each hose separately takes to fill the same pool.
# #### version 1 - quite verbose! ####

# Time taken to fill pool in hours
timeGreen = 1.5
timeRed  = 1.2

# Convert hours to minutes
minutesGreen = 60 * timeGreen
minutesRed = 60 * timeRed

# Rate each hose takes to fill the pool
rateHoseGreen = 1 / minutesGreen
rateHoseRed = 1 / minutesRed

# Rate it takes to fill the pool using both hoses
rateCombined = rateHoseGreen + rateHoseRed

# Time it takes to fill pool using both hoses in minutes
timeToFillPool = 1 / rateCombined
print(timeToFillPool)
