import turtle
n = 1440
turtle.speed(1000)
b = 90
angle = (360/n)
for i in range(n):
    turtle.forward(720/n)
    turtle.right(angle)
for i in range(1):
    turtle.right(b)
    turtle.forward(230)
    turtle.right(2*b)
    turtle.forward(115)
    turtle.right(b)
    turtle.forward(115)
    turtle.right(2*b)
    turtle.forward(230)
turtle.exitonclick()
