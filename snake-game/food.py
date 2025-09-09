from turtle import Turtle
import random

# define a new food class
class Food(Turtle): # inherit attributes from the turtle class

    # define an initialisation function
    def __init__(self):
        super().__init__()
        self.penup() # raise the pen
        self.color("blue") # set the shape colour
        self.shape("circle") # set the shape
        self.shapesize(.5, .5) # set the shape size
        self.speed("fastest") # set the movement speed
        random_x = random.randint(-200, 200)  # set random x coordinates
        random_y = random.randint(-200, 200)  # set random y coordinates
        self.goto(random_x, random_y) # send the shape to the random coordinates

    def refresh(self):
        self.goto(random.randint(-200, 200), random.randint(-200, 200))

