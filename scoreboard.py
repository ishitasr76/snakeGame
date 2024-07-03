from turtle import Turtle
class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            content = data.read()
            self.high_score = int(content)

        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto (0,270)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", False, "center", ("Courier", 20, "bold"))

    def increase_score(self):
        self.score +=1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open ("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.update_score()
    #     self.goto (0,0)
    #     self.write(f"Game Over!", False, "center", ("Courier", 20, "bold"))
