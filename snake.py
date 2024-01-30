import turtle as t

MOVE_DISTANCE = 20


# STARTING_POSITION = [(0,0),(-20,0),(-40,0)]: permite cambiar la posición inicial. No obstante,
# se puede ajustar con un random

class Snake:

    # Snake body creation:
    def __init__(self):
        self.size_of_body = 3
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):

        for i in range(self.size_of_body):
            new_part = t.Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(x=-20 * i, y=0)
            self.snake_parts.append(new_part)
    def extend(self):
        new_part = t.Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.snake_parts[-1].position())
        self.snake_parts.append(new_part)

    def move(self):

        for i in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[i - 1].xcor()
            new_y = self.snake_parts[i - 1].ycor()
            self.snake_parts[i].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.left(-90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.right(-90)

# game_is_on = True
#
# while game_is_on:
#     # Updating the screen
#
# time.sleep(0.1)
#     screen.update()

# screen.exitonclick()

# Solución diferente a la del curso para los giros, tomando una instantánea de las posiciones y actualizándolas con
# base en esta instantánea

# while game_is_on:
#
#     positions = []
#
#     for j in snake_parts:
#         positions.append(j.position())
#
#     print(positions)
#
#     for i in range(-len(snake_parts) + 1, 0, 1):
#         # Updating positions starting from head:
#
#         new_coordinate = positions[i-1]
#         snake_parts[i].goto(x = new_coordinate[0], y = new_coordinate[1])
#
#     snake_parts[0].forward(20)
#     snake_parts[0].left(90)
#
#     time.sleep(0.1)
#     screen.update()


# positions = []

# Personal exercise for turning each part:

# for i in range(len(snake_parts)):
#     initial_position = snake_parts[i].position()
#     positions.append(initial_position)
#
# while game_is_on:
#
#     # Defining initial positions:
#
#     print(positions)
#
#     # Changing direction of head and updating new position at the end of the list positions:
#
#     snake_parts[0].left(90)
#     snake_parts[0].forward(20)
#     new_position_head = snake_parts[0].position()
#     positions.append(new_position_head)
#     print(positions)
#
#     # Updating positions of the tail:
#
#     snake_parts[1].goto(x = positions[0][0], y = positions[0][1])
#     snake_parts[2].goto(x=positions[1][0], y=positions[1][1])
#
#     # Updating positions list:
#
#     positions[0] = new_position_head
#     print(positions[0])
#     positions[1] = snake_parts[1].position()
#     positions[2] = snake_parts[2].position()

# Updating the screen

# time.sleep(0.1)
# screen.update()
