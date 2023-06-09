from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.screensize(canvwidth=600, canvheight=600)

paddle_r = Paddle((320, 0))
paddle_l = Paddle((-320, 0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_l.go_up, "Up")
screen.onkeypress(paddle_l.go_down, "Down")
screen.onkeypress(paddle_r.go_up, "w")
screen.onkeypress(paddle_r.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.refresh_rate)
    screen.update()
    ball.move()

    # detect collision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # paddle collision
    if ball.distance(paddle_r) < 50 and ball.xcor() > 250 or ball.distance(paddle_l) < 50 and ball.xcor() < -250:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.point_l()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.point_r()







screen.exitonclick()


