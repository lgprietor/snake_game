import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake game by Luisgap")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()