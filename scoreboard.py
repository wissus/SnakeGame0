from turtle import Turtle

ALIGNEMENT = "center"
FONT = "courier"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-90, 280)
        self.write(f"score: {self.score}", align=ALIGNEMENT, font=FONT)
        self.goto(90, 280)
        self.write(f"highscore : {self.high_score}", align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
