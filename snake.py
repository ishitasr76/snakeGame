from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]
    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)
    def move(self):
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            newx = self.all_snakes[seg_num - 1].xcor()
            newy = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(newx, newy)
        self.all_snakes[0].forward(MOVE_DISTANCE)
    def add_segment(self,position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        # last_snake= self.all_snakes[len(self.all_snakes)-1]
        # locationx = last_snake.xcor()
        # locationy = last_snake.ycor()
        # if last_snake.heading()==UP:
        #     snake.goto(locationx, locationy-20 )
        # elif last_snake.heading() == DOWN:
        #     snake.goto(locationx, locationy +20)
        # elif last_snake.heading() == RIGHT:
        #     snake.goto(locationx-20, locationy)
        # elif last_snake.heading() == UP:
        #     snake.goto(locationx+ 20, locationy)
        snake.goto(position)
        self.all_snakes.append(snake)
    def extend_snake(self):
        self.add_segment(self.all_snakes[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for snake in self.all_snakes:
            snake.goto(1000,1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

