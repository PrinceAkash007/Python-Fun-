import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=200
h=0
for i in range(360):
    t.begin_fill()
    for j in range(2):
        
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h+=1/n
        t.color(c)
        t.left(20)
        t.forward(i-1)
    t.end_fill()