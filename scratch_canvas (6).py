import turtle
import random

dict1 = {'Shape1': 'square', 'Shape2': 'triangle', 'Shape3': 'circle'}
colors = ['orange', 'red', 'green', 'blue', 'yellow']

user_input = input('enter the desired shape:')

turtle.fillcolor(random.choice(colors))

turtle.begin_fill()
if dict1.get("Shape1") == user_input: 
    for i in range (0,4):
        turtle.forward(100)
        turtle.left (90)
elif dict1.get("Shape2") == user_input:
    for i in range (0,3):
        turtle.forward(100)
        turtle.left (120)
elif dict1.get("Shape3")==user_input:
      turtle.circle(100)
else:
       print("Enter a value between square, circle and triangle")

turtle.end_fill() 
