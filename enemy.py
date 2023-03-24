from turtle import Turtle
import random

position = [-150, -100, -50, 0, 50, 100, 150]


class Enemy:

    def __init__(self):
        super().__init__()
        self.line = []
        self.a = 20
        self.bullets = []

    def creat_enemy_line(self, y):
        for pos in position:
            turtle = Turtle()
            turtle.pu()
            turtle.color("purple")
            turtle.shape("square")
            turtle.shapesize(stretch_wid=0.5, stretch_len=1.5)
            turtle.goto(pos, y)
            self.line.append(turtle)

    def enemy_move_right(self):
        for pos in self.line[::-1]:
            new_x = pos.xcor() + self.a
            new_y = pos.ycor() - 0.1
            pos.goto(x=new_x, y=new_y)

    def enemy_bounce(self):
        self.a *= -1

    def create_bullet(self):
        random_number = random.randint(1, 6)
        if random_number == 4:
            bullet = Turtle()
            bullet.pu()
            bullet.color("red")
            bullet.shape("square")
            bullet.shapesize(stretch_len=0.2, stretch_wid=0.5)
            ship = random.choice(self.line)
            x = ship.xcor()
            y = ship.ycor()
            bullet.goto(x, y)
            self.bullets.append(bullet)

    def move_bullet(self):
        for bullet in self.bullets:
            x = bullet.xcor()
            y = bullet.ycor() - 15
            bullet.goto(x, y)
