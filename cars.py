from turtle import Turtle, colormode
from random import randrange
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

colormode(255)


def rand_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return r, g, b


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()

    def create_cars(self, MAX_CARS):
        if len(self.car_list) < MAX_CARS:
            for i in range(MAX_CARS):
                a = "car" + f"{i}"
                a = Turtle(shape="square")
                a.penup()
                a.shapesize(stretch_wid=1, stretch_len=2)
                a.color(rand_color())
                a.setheading(180)
                a.goto(x=randrange(320, 1500), y=randrange(-250, 290))
                a.speed("slowest")
                self.car_list.append(a)
        else:
            self.reuse_cars()

    def move_cars(self, CAR_SPEED):
        if self.car_list:
            for i in range(len(self.car_list)):
                self.car_list[i].forward(CAR_SPEED)

    def reuse_cars(self):
        if self.car_list:
            for i in range(len(self.car_list)):
                if self.car_list[i].xcor() < -320:
                    self.car_list[i].hideturtle()
                    self.car_list[i].goto(x=randrange(500, 1500), y=randrange(-250, 290))
                    self.car_list[i].showturtle()
        else:
            print("something broke")




