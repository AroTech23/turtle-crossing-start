import random
from turtle import  Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.create_car()
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append( new_car )
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)


    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def remove_offscreen_cars(self):
        self.all_cars = [car for car in self.all_cars if car.xcor () > -320]

