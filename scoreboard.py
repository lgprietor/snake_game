import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.write(arg = f"Score: {self.points}", move = False, align="center", font=("Courier",18,"normal"))

    def add_score(self):
        self.clear()
        self.points += 1
        self.write(arg=f"Score: {self.points}", move=False, align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game over", move=False, align="center", font=("Courier", 18, "normal"))

