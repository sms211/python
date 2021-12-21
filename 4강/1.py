import turtle as t

n = 5
t.shape("classic")
t.color("skyblue")
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()
