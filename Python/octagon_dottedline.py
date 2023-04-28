import turtle

turtle.setup(width = 600, height = 600)

t = turtle.Pen()

edges = 8
dot_size = 70

for i in range(edges):
    for j in range(0, 20, 2):
            t.forward(1)
            t.penup()
            t.forward(5)
            t.pendown()
    t.right(45)
