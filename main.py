from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

game_is_on = True

wonu = Snake()
wonu_food = Food()
wonu_score = Scoreboard()

screen.listen()
screen.onkey(wonu.up, "Up")
screen.onkey(wonu.down, "Down")
screen.onkey(wonu.left, "Left")
screen.onkey(wonu.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    wonu.move()

    # collision with food

    if wonu.head.distance(wonu_food) < 15:
        wonu_food.refresh()
        wonu.extend()
        wonu_score.increase_score()

    # collision with wall
    if wonu.head.xcor() > 290 or wonu.head.xcor() < -290 or wonu.head.ycor() > 290 or wonu.head.ycor() < -290:
        wonu_score.reset()
        wonu.reset()

    # collision with tail
    for i in wonu.new_snake[1:]:
        if wonu.head.distance(i)<10:
            wonu_score.reset()
            wonu.reset()
screen.exitonclick()
