from turtle import * #type:ignore
import random

getscreen().bgcolor("#000000")
color("white",'yellow')
speed(10)

# Star Making 
def draw_star(size):
    for _ in range(5):
        forward(size)
        left(216)

for _ in range(50):
    x,y = random.randint(-300,300), random.randint(-300,300)
    
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    draw_star(random.randint(5,25))
    end_fill()

done()