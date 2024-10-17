from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setx(x_cor)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def move_paddle_up(self):
        self.setheading(90)
        if self.ycor() < 240:
            self.forward(40)

    def move_paddle_down(self):
        self.setheading(270)
        if self.ycor() > -230:
            self.forward(40)
