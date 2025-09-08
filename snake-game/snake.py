from turtle import Turtle

# define the move distance
MOVE_DISTANCE = 20
# define the starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# define the movement headings
DOWN = 270
LEFT = 180
RIGHT = 0
UP = 90


# create a snake class
class Snake:

    # create an initialisation function
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create a function to initialise the segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # set the segment shape
            new_segment.color("white")  # set the segment colour
            new_segment.penup()  # raise the pen
            new_segment.goto(position)  # send segment to starting position
            self.segments.append(new_segment)  # add segment to the list

    # create a function to handle movement
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()  # retrieve the x coordinates of the previous segment
            new_y = self.segments[segment_number - 1].ycor()  # retrieve the y coordinates of the previous segment
            self.segments[segment_number].goto(new_x, new_y)  # move each segment to the positions of the previous segment

        self.head.forward(MOVE_DISTANCE)  # move the first segment forward

    # create a heading to change direction up
    def up(self):
        if self.head.heading() != DOWN: # snake cannot 180
            self.head.setheading(UP)

    # create a heading to change direction down
    def down(self):
        if self.head.heading() != UP: # snake cannot 180
            self.head.setheading(DOWN)

    # create a heading to change direction left
    def left(self):
        if self.head.heading() != RIGHT: # snake cannot 180
            self.head.setheading(LEFT)

    # right
    def right(self):
        if self.head.heading() != LEFT: # snake cannot 180
            self.head.setheading(RIGHT)