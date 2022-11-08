from turtle import Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.goto(250, 250)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def score_board(self):
        self.score += 1
        self.update_scoreboard()

    def level_board(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 50, "normal"))
