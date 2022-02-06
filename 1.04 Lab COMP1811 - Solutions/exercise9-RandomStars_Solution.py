# Draws 15 5 corner stars at random positions.

import turtle
import random

# Program constants
MAX_NUM_STARS = 15    # Number of stars to draw
MIN_POSITION  = -300  # in pixels
MAX_POSITION  = 300
MIN_STAR_SIZE = 5     # in pixels
MAX_STAR_SIZE = 180
ANIMATION_SPEED = 0  # Animation speed (speed is a value from 0..10, where
                     # 0 is fastest; 10 is fast; 6 is normal; 3 is; 1 is slowest

# Program variables
angle = 144          # Angle to turn

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

for n in range(MAX_NUM_STARS):
    turtle.penup()
    turtle.goto(random.randint(MIN_POSITION, MAX_POSITION), random.randint(MIN_POSITION, MAX_POSITION))
    turtle.pendown()
    star_size = random.randint(MIN_STAR_SIZE, MAX_STAR_SIZE)
    for i in range (1,6):
       turtle.left(angle)
       turtle.forward(star_size)

turtle.exitonclick()  # waits until you click on the turtle window to close it.
