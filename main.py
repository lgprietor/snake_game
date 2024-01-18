import turtle as t
import time

screen = t.Screen()
screen.setup(height=600, width=600)

screen.bgcolor("black")
screen.title("Snake game by Luisgap")

size_of_body = 3
snake_parts=[]
screen.tracer(0)


for i in range(size_of_body):
    new_part = t.Turtle("square")
    new_part.color("white")
    new_part.penup()
    new_part.goto(x=-20*i,y=0)
    snake_parts.append(new_part)

screen.update()

game_is_on = True

while game_is_on:
    for i in snake_parts:

        i.forward(10)

    time.sleep(0.1)
    screen.update()


















screen.exitonclick()