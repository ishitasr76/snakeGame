from turtle import Turtle
import random
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5)
        self.color("pink")
        self.speed ("fastest")
        self.new_food()


    def new_food(self):
        randX = random.randint(-280, 280)
        randY = random.randint(-280, 280)
        self.goto(randX, randY)