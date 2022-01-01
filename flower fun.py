import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
colour = ('yellow','red','pink','cyan','light green','orange')

for i in range(150):
    t.pencolor(colour[i%6])
    t.circle(190-i/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)


s.exitonclick()
