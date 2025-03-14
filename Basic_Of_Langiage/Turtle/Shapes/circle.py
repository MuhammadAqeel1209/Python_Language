import turtle

turtle.bgcolor("black")
colors = ['red','dark red']

for num in range(400):
    turtle.forward(num+1)
    turtle.right(89)
    turtle.pencolor(colors[num%2])
    
turtle.done()