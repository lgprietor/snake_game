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

    # Detect collisions with tail:
    # If head collides with any segment in the tail trigger game over sequence:

    # for i in range(len(snake.snake_parts)-1, 0, -1):
    #
    #     if snake.head.distance(snake.snake_parts[i]) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()


# Module - Detect collisions with tail - Using position
# print(f"Snake body part {i+1} position: {snake.snake_parts[i].position()}")
# print(snake.snake_parts[i].position() == snake.snake_parts[0])
#
# if snake.head.xcor() == -0:
#     snake.head.setx(0)
#     print(snake.head.position())
#
# if snake.head.ycor() == -0:
#     snake.head.sety(0)
#     print(snake.head.position())
#
# # print(snake.snake_parts[i].xcor())
# # print(snake.head.xcor())
# # print(snake.snake_parts[i].ycor())
# # print(snake.head.ycor())
#
# if (round(snake.snake_parts[i].xcor()) == round(snake.head.xcor()) and round(snake.snake_parts[i].ycor())
#         == round(snake.head.ycor())):
#     print(snake.snake_parts[i].xcor())
#     print(snake.head.xcor())
#     print(snake.snake_parts[i].ycor())
#     print(snake.head.ycor())
#     game_is_on = False
#     scoreboard.game_over()
