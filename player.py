from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.color("yellow")
        self.goto(0, -270)
        self.bullets = []

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def refresh(self):
        self.goto(0, -270)

    def create_bullet(self):
        bullet = Turtle()
        bullet.pu()
        bullet.color("green")
        bullet.shape("square")
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.5)
        x = self.xcor()
        y = self.ycor()
        bullet.goto(x, y)
        self.bullets.append(bullet)

    def move_bullet(self):
        for bullet in self.bullets:
            x = bullet.xcor()
            y = bullet.ycor() + 15
            bullet.goto(x, y)
