from turtle import Turtle, Screen
from random import random, randint

CURSOR_SIZE = 20

def my_circle(color):
    radius = randint(10, 50)

    circle = Turtle('circle', visible=False)
    circle.shapesize(radius / CURSOR_SIZE)
    circle.color(color)
    circle.penup()

    while True:
        nx = randint(2 * radius - width // 2, width // 2 - radius * 2)
        ny = randint(2 * radius - height // 2, height // 2 - radius * 2)

        circle.goto(nx, ny)

        for other_radius, other_circle in circles:
            if circle.distance(other_circle) < 2 * max(radius, other_radius):
                break  # too close, try again
        else:  # no break
            break

    circle.showturtle()

    circle.onclick(lambda x, y, t=circle: t.hideturtle())  # expand this into a complete function

    return radius, circle

screen = Screen()
screen.bgcolor("lightgreen")
screen.title("clicky")

width, height = screen.window_width(), screen.window_height()

circles = []

for _ in range(0, 20):
    rgb = (random(), random(), random())

    circles.append(my_circle(rgb))

screen.mainloop()