from turtle import *  # Importing all functions from the turtle module
import random  # Importing the random module for generating random values

# Setting the outline color to red and the fill color to blue
color('red', 'blue')

# Function to draw a square of a given size
def square(size):
    forward(size)  # Move forward by size units
    left(90)  # Turn left by 90 degrees
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)

# Uncomment the following code to draw and fill two squares
# begin_fill()  # Start filling the shape
# square(200)  # Draw a square of size 200
# end_fill()  # Stop filling the shape

# penup()  # Lift the pen to move without drawing
# forward(200)  # Move forward by 200 units
# pendown()  # Put the pen down to start drawing
# begin_fill()
# square(200)
# end_fill()

# Uncomment the following code to create a black background with white and yellow stars
# getscreen().bgcolor("#000000")  # Set the screen background color to black
# color("white", 'yellow')  # Set the pen color to white and fill color to yellow
# speed(10)  # Set the speed of drawing

# # Function to draw a star with a given size
# def draw_star(size):
#     for _ in range(5):  # Loop 5 times to create a star shape
#         forward(size)  # Move forward by size units
#         left(216)  # Turn left by 216 degrees

# # Loop to create 50 randomly placed stars
# for _ in range(50):
#     x, y = random.randint(-300, 300), random.randint(-300, 300)  # Generate random coordinates
    
#     penup()  # Lift the pen to move without drawing
#     goto(x, y)  # Move to the random coordinates
#     pendown()  # Put the pen down to start drawing
#     begin_fill()  # Start filling the shape
#     draw_star(random.randint(5, 25))  # Draw a star of random size between 5 and 25
#     end_fill()  # Stop filling the shape


done()  # Finish the drawing and keep the window open
