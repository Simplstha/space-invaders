from turtle import Screen
import time
from enemy import Enemy
from player import Player
from result import Result

game = True
position = [250, 230, 210, 190, 170, 150]
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
enemy_ship = Enemy()
player = Player()
result = Result()
result.write_lives()
# enemy_line = []
for pos in position:
    line = enemy_ship.creat_enemy_line(pos)
    # enemy_line.append(line)
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.create_bullet, "Up")
while game:
    time.sleep(0.1)
    screen.update()
    enemy_ship.enemy_move_right()
    enemy_ship.create_bullet()
    enemy_ship.move_bullet()
    player.move_bullet()
    for bullet in enemy_ship.bullets:
        if player.distance(bullet) < 15:
            player.refresh()
            bullet.goto(-800, -2000)
            result.count_decrease()
            result.write_lives()
            if result.life_count == 0:
                result.game_over()
                game = False
    try:
        if enemy_ship.line[-1].xcor() > 350 or enemy_ship.line[0].xcor() < -350:
            enemy_ship.enemy_bounce()
        for ship in enemy_ship.line:
            if ship.ycor() < -260:
                result.game_over()
                game = False
            for bullet in player.bullets:
                if ship.distance(bullet) < 12:
                    ind = enemy_ship.line.index(ship)
                    del enemy_ship.line[ind]
                    ship.goto(-2000, -2000)
                    bullet.goto(2000, -2000)
    except IndexError:
        result.you_won()
        game = False

screen.exitonclick()