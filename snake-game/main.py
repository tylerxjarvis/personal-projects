from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

screen = Screen() # create the screen object
screen.setup(width=600, height=600) # configure the screen dimensions
screen.bgcolor("black") # set the screen colour
screen.title("Snake Game") # set the screen window title
screen.tracer(0) # disable automatic screen updates

food = Food() # create the new food object
scoreboard = Scoreboard() # create a new scoreboard object
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

    # define a way to refresh the food upon collision
    if snake.head.distance(food) < 15:
        food.refresh() # refresh the food
        scoreboard.increase_score() # increase the score

# exit the screen
screen.exitonclick()