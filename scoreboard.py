from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(-100, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(self.left_score, align="center", font=("Arial", 30, "normal"))
        self.goto(100, 280)
        self.write(self.right_score, align="center", font=("Arial", 30, "normal"))

    def point_l(self):
        self.left_score += 1
        self.update_scoreboard()

    def point_r(self):
        self.right_score += 1
        self.update_scoreboard()