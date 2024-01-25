import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)

        self.write(arg = "Hello", move = False, align="center", font=("Arial",12,"normal"))


