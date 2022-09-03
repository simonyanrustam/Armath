from turtle import *
from random import *

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(0)

for i in range(70):
  rgb = [randint(0, 255), randint(0, 255), randint(0, 255)]
  x = randint(- 200, 200)
  y = randint(- 200, 200)
  s = randint(5, 25)
  draw_circle(tommy, rgb, s, x, y)
