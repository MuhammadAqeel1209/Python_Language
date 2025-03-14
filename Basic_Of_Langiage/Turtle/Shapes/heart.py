import math
import turtle


def heartRa(k):
    return 12 * math.sin(k)**3

def heartRb(k):
    return 12 *math.cos(k)-5*\
        math.cos(2 *k)-2*\
        math.cos(3 *k)-\
        math.cos(4 * k)
turtle.speed(4000)

turtle.bgcolor("black") 
for i in range(6000):
    turtle.goto(heartRa(i)*20,heartRb(i)*20)
    for j in range(5):
        turtle.color("red")

turtle.goto(0,0)
turtle.done()   