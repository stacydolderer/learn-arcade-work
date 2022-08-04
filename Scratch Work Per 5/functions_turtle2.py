import turtle
bob = turtle.Turtle()
#xcor, ycor , size, pen color, fill color
def square(x, y, s, p, c):
    poly(x, y, s, 4, p, c)

def triangle(x, y, s):
    poly(x, y, s, 3, "red", "black")

#xcor, ycor, size, sides, pen, fill
def poly(x, y, sz, sd, p, c):
    bob.up()
    bob.goto(x, y)
    bob.down()
    bob.color(p, c)
    bob.begin_fill()
    for i in range(sd):
        bob.forward(sz)
        bob.left(360/sd)
    bob.end_fill()

poly(300, 300, 70, 6, "yellow", "purple")
square(100, 100, 100, "green", "blue")
square(25, 25, 50, "red", "yellow")
triangle(250, 100, 100)