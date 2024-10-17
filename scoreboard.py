from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Impact', 80, 'normal')


# other fonts
# 'Arial Black'
# 'Impact'
# 'Verdana'
# Trebuchet MS

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 200)
        self.write("|", True, align=ALIGNMENT, font=FONT)
        self.goto(-75, 200)
        self.write(f"{self.left_score}", True, align=ALIGNMENT, font=FONT)
        self.goto(75, 200)
        self.write(f"{self.right_score}", True, align=ALIGNMENT, font=FONT)
