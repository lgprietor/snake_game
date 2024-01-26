import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.points}", move=False, align="center", font=("Courier", 15, "normal"))

    def refresh_screen(self):
        self.points += 1
        self.write(arg=f"Score: {self.points}", move=False, align="center", font=("Courier", 15, "normal"))









