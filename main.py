import turtle
n = 1440
#any numerical value works for n
turtle.speed(1000)
b = 90
#b is supposed to be 90 in order to create the crosshatch in the circle
def cheese(z, w):
    angle = z/w
    return angle
#this changes the length and decides the sides to the shape to create the perf. circle
def calc_area(base, height):
    area= base * height
    return area
#calc_area is important for outside square
for i in range(n):
    turtle.forward(720/n)
    turtle.right(cheese(360, n))
for i in range(1):
    turtle.right(b)
    turtle.forward(230)
    turtle.right(2*b)
    turtle.forward(115)
    turtle.right(b)
    turtle.forward(115)
    turtle.right(2*b)
    turtle.forward(230)
turtle.right(b)
turtle.forward(calc_area(230, 230)**(0.5)/2)
for i in range(2):
    turtle.right(b)
    turtle.forward((calc_area(230, 230)**(0.5)))
turtle.right(b)
turtle.forward(calc_area(230, 230)**(0.5)/2)
turtle.forward(calc_area(230, 230)**(0.5)/2)
turtle.right(b)
turtle.forward(calc_area(230, 230)**(0.5)/2)

turtle.exitonclick()
