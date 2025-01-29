import math
from turtle import * # type: ignore

from pyparsing import col

def heartRa(k):
    return 12 * math.sin(k)**3

def heartRb(k):
    return 12 *math.cos(k)-5*\
        math.cos(2 *k)-2*\
        math.cos(3 *k)-\
        math.cos(4 * k)
speed(4000)

bgcolor("black") 
for i in range(6000):
    goto(heartRa(i)*20,heartRb(i)*20)
    for j in range(5):
        color("red")

goto(0,0)
done()   