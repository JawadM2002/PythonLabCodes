# Draws a design using repeated circles using Python's turtle module.

import turtle

# Program constants
MAX_NUM_CIRCLES = 24# Number of circles to draw
ANGLE = 15          # Angle to turn
ANIMATION_SPEED = 0 # Animation speed
MAX_NUM_DESIGNS = 3 # Maximum number or nested design to produce a design similar to image b.2 in the exercise sheet.

# Program variables
radius = 100        # Radius of each circle

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Solution1
# Draw 24 circles, with the turtle tilted by 15 degrees after each circle is drawn.
for x in range(MAX_NUM_CIRCLES):
    turtle.circle(radius)
    turtle.left(ANGLE)

# generate inner design 1 by reducing radius
radius = 50
for x in range(MAX_NUM_CIRCLES):
    turtle.circle(radius)
    turtle.left(ANGLE)

# generate inner design 2 by reducing radius again
radius =25
for x in range(MAX_NUM_CIRCLES):
    turtle.circle(radius)
    turtle.left(ANGLE)

turtle.exitonclick()  # waits until you click on the turtle window to close it.
