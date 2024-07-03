import time
import turtle
from turtle import Turtle,Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
turtle.title("Snake Game :)")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right" )

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        score.increase_score()
        snake.extend_snake()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        # game_is_on = False
        score.reset_score()
        snake.reset_snake()

    for segment in snake.all_snakes:
        if segment != snake.head:
            if snake.head.distance(segment)<10:
                # game_is_on = False
                score.reset_score()
                snake.reset_snake()

screen.exitonclick()