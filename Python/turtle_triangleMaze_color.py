import turtle

turtle.setup(width = 500, height = 500)
t = turtle.Pen()
t.pencolor("blue")
t.width(3)

for i in range(0, 301, 8):
    t.forward(i)
    t.left(120)

