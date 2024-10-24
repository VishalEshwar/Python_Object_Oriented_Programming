from turtle import *

# Create Turtle instances
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

def triangle(t, color):
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.left(120)
    t.end_fill()  # Correct indentation

# List of turtle instances
turtles = [t1, t2, t3, t4]
y = 100

# Position turtles
for t in turtles:
    t.up()
    t.goto(0, y)
    t.down()
    y -= 100

# Draw triangles with different colors
triangle(t1, "red")
triangle(t2, "black")
triangle(t3, "pink")
triangle(t4, "blue")

done()
