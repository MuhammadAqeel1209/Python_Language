from  turtle import * #type:ignore

bgcolor("black")
colors = ['red','dark red']

for num in range(400):
    forward(num+1)
    right(89)
    pencolor(colors[num%2])
    
done()