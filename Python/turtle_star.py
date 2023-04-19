import turtle

turtle.setup(width = 600,height = 600)

t = turtle.Pen()
t.goto(-50, 0)
t.color("blue", "yellow")
t.width(5)

t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(360/5*2)
t.end_fill()

t.done()


