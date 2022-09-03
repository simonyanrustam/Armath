import turtle
import random

window = turtle.Screen()
window.bgcolor("yellow")
turtle.speed(0)
turtle.hideturtle()

colors_lst = ["darkblue", "red", "magenta", "teal" "darkcyan", "gray", "indigo", "darkviolet"]

def createStar(step, angle):
  for i in range(5):
    turtle.color(colors_lst[random.randint(0, len(colors_lst) - 1)])
    turtle.forward(step)
    turtle.right(angle)

for i in range(70):
  turtle.penup()
  turtle.setpos(random.randint(-300, 200), random.randint(-200, 200))
  turtle.pendown()
  createStar(20, 144)
