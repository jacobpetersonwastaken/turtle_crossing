from turtle import Turtle, colormode
STARTING_POSITION = [(0, 0)]
MOVE_DISTANCE = 20
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.goto(x=0, y=-290)
    

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

