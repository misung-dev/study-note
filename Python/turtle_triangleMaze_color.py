import turtle

turtle.setup(width = 500, height = 500)
t = turtle.Pen()
colors = ["red", "blue", "green", "black"]
t.width(3)

for i in range(0, 200, 5):
    t.forward(i)
    t.left(120)
    t.pencolor(colors[i%4])
