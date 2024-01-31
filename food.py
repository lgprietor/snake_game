import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-260, 260)
        new_y = random.randint(-260, 260)
        self.goto(x=new_x, y=new_y)