from turtle import *
from random import randint

# Initialize turtle
pencil = Turtle()
Screen().colormode(255)  # Allow RGB colors with values from 0 to 255

for _ in range(4):
    # Generate random colors
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color1 = (r, g, b)

    # Generate random position
    x = randint(-200, 200)
    y = randint(-200, 200)

    pencil.up()
    pencil.goto(x, y)
    pencil.down()

    pencil.color(color1)
    pencil.begin_fill()
    
    # Draw square
    for _ in range(4):
        pencil.fd(100)
        pencil.rt(90)

    pencil.end_fill()  # Move this outside the inner loop

done()
