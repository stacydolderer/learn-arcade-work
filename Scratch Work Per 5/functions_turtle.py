import turtle
draw = turtle.Turtle()

#x, y, size, color
def square(x, y, s, c):
    poly(x, y, s, 4, c)
        
#x, y, size, number sides, color
def poly(x, y, s, n, c):
    draw.pu()
    draw.goto(x,y)
    draw.pd()
    draw.color(c)
    draw.begin_fill()
    for i in range(n):
        draw.forward(s)
        draw.right(360/n)
    draw.end_fill()
      
poly(20, 20, 20, 8, 'purple')
poly(220, 220, 30, 3, 'purple')
square(100, 100, 100, 'green')
square(50, 50, 200, 'blue')