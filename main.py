import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("lightgrey")

screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()
screen.listen()
screen.onkey(player.up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    car_manager.remove_offscreen_cars()
    #detects collision with car
    for car in car_manager.all_cars:
        if abs ( player.xcor () - car.xcor () ) < 20 and abs ( player.ycor () - car.ycor () ) < 20:
            scoreboard.game_over()


            game_is_on=False

    #detects a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_level()





screen.exitonclick()

screen.mainloop()

