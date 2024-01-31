import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake game by Luisgap")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect collisions with tail:
    # If head collides with any segment in the tail trigger game over sequence:

    for i in range(len(snake.snake_parts) - 1, 0, -1):
        # print(f"Snake's head position: {snake.head.position()}")
        # print(f"Snake body part {i} position: {snake.snake_parts[i].position()}")
        #
        # print(snake.head.position() == snake.snake_parts[i].position())

        # print(f"Snake's head position: {snake.head.position()}")

        if snake.head.position() == snake.snake_parts[i].position():
            game_is_on = False
            scoreboard.game_over()

    snake.move()

    # Detect collisions with the food:

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    # Detect collisions with wall:

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()






screen.exitonclick()