
from turtle import Turtle

FONT = ('Arial', 15, 'normal')

class State(Turtle):

    def __init__(self,state_name,x_cord,y_cord):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x_cord, y_cord)
        self.write(state_name,False,"center",FONT)
