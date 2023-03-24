from turtle import Turtle


class Result(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("pink")
        self.life_count = 3

    def game_over(self):
        self.goto(-200, 0)
        self.write("Game Over!", font=("Courier", 60, "bold"))

    def you_won(self):
        self.goto(-200, 0)
        self.write("You Won!!!", font=("Courier", 60, "bold"))

    def count_decrease(self):
        self.life_count -= 1

    def write_lives(self):
        self.clear()
        self.goto(210, 270)
        self.write(f"Lives:{self.life_count}", font=("Courier", 20, "bold"))
