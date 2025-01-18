# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression
# This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.
# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

a = True
print(a:= False)

number = [1,2,3,4,5]
while(n:= len(number) > 0 ):
    print(number.pop())
"""
# Without Varlus Operator 👇👇👇
foods = list()
while True:
    food = input("Enter the food do you want and enter \"quit\" for stop\t") 
    if food == "quit":
        break
    foods.append(food)"""

# With Varlus Operator 👇👇👇
foods = list()
while food:=input("Enter the food do you want and enter \"quit\" for stop\t") != "quit":
    foods.append(food)
