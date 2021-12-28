import turtle as t
import random


t.shape("turtle")
t.speed(-1)
t.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "skyblue", "blue", "purple"]


for x in range(500):
    color = random.choice(colors)
    t.pencolor(color)
    a = random.randint(1, 360)
    t.setheading(a)
    b = random.randint(1, 20)
    t.fd(b)
