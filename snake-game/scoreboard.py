from turtle import Turtle

# define the alignment
ALIGNMENT = "center"
# define the font
FONT = ("Arial", 18, "bold")

# define a new scoreboard class
class Scoreboard(Turtle):

    # define an initialisation function
    def __init__(self):
        super().__init__()
        self.color("white") # set the colour
        self.hideturtle() # hide the turtle
        self.penup() # raise the pen
        self.goto(0, 270) # move to the position
        self.score = 0 # set the starting score
        self.update_scoreboard() # update the scoreboard

    # define a scoreboard increase function
    def increase_score(self):
        self.score += 1 # increase the starting score value by one
        self.clear() # clear the scoreboard
        self.goto(0, 270)  # move to the position
        self.update_scoreboard() # update the scoreboard

    # define a scoreboard update function:
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)  # set the scoreboard appearance