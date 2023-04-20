import turtle
turtle.setup(width = 500, height = 500)

t = turtle.Pen()
t.width(10)
t.pencolor("pink")

for i in [1,3,6,10,0] :
    t.speed(i)
    t.forward(150)
    t.right(72)

t.pencolor("red")
speed_string = ['slowest', 'slow', 'normal', 'fast', 'fastest']
for i in speed_string :
    t.speed(i)
    t.forward(150)
    t.right(72)
    
