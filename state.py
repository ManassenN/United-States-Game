from turtle import Turtle

class State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def create_state(self,coo,state):
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(coo)
        self.write(state, align="center", font=("Courier", 8, "bold"))






