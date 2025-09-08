from snake import Snake
from turtle import Screen, Turtle
import time

screen = Screen() # create the screen object
screen.setup(width=600, height=600) # configure the screen dimensions
screen.bgcolor("black") # set the screen colour
screen.title("Snake Game") # set the screen window title
screen.tracer(0) # disable automatic screen updates

snake = Snake() # create a new snake object

screen.listen() # start listening for user key input
screen.onkey(snake.up, "Up") # move up
screen.onkey(snake.down, "Down") # move down
screen.onkey(snake.left, "Left") # move left
screen.onkey(snake.right, "Right") # move right

game_over = False # initialise the game

# start the game
while not game_over:
    screen.update() # update the screen
    time.sleep(0.1) # implement sleep to reduce motion lag
    snake.move()  # move the snake

# exit the screen
screen.exitonclick()