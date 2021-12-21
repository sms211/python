import turtle as t
import random


t.bgcolor("black")



a = 0
b = 0
t.speed(-1)

t.penup()
t.goto(0, 200)
t.pendown()

colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

while(True):
    color = random.choice(colors)
    t.pencolor(color)
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()

t.done()
