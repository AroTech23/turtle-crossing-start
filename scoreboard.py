from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=1
        self.penup()
        self.goto(-280,270)
        self.write(f"Level:{self.level}",align="left",font=FONT)
    def update_level(self):
        self.level += 1
        self.clear()
        self.write ( f"Level:{self.level}" , align="left" , font=FONT )
    def game_over(self):
        self.goto ( 0 , 0 )
        self.color ( "red" )
        self.write ( "Game Over" , align="center" , font=("Courier" , 30 , "bold") )

