import turtle as t

t.bgcolor("green")
n = 5
t.color("skyblue")
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()
