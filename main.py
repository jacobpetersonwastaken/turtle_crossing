from turtle import colormode, Screen, onscreenclick
from scoreboard import Scoreboard
from cars import Car
from player import Player
import time
import random
game_is_on = True
colormode(255)
MAX_CARS = 35
CAR_SPEED = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_POSITION = [((-1 * (SCREEN_WIDTH/2)) + 50, 0), ((SCREEN_WIDTH/2) - 50, 0)]

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("grey")
screen.title("frogger")
screen.tracer(0)
scoreboard = Scoreboard()
cars = Car()
player = Player()
screen.onkeypress(key='Up', fun=player.up)

while game_is_on:
    time.sleep(.1)
    cars.create_cars(MAX_CARS)
    cars.move_cars(CAR_SPEED)

    for i in cars.car_list:
        if player.distance(i) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > SCREEN_HEIGHT/2:
        scoreboard.score_board()
        scoreboard.level_board()
        player.goto(x=0, y=-290)
        CAR_SPEED += 5

    screen.update()
    screen.listen()

screen.exitonclick()