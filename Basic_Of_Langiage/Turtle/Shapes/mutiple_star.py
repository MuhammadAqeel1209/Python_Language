import turtle
import random

turtle.getscreen().bgcolor("#000000")
turtle.color("white",'yellow')
turtle.speed(10)

# Star Making 
def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.left(216)

for _ in range(50):
    x,y = random.randint(-300,300), random.randint(-300,300)
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    draw_star(random.randint(5,25))
    turtle.end_fill()

turtle.done()