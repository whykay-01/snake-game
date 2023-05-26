import pygame
import random
import time

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("python-files/icon.png")
pygame.display.set_icon(icon)

# snake
# TODO: have a look at this part: might be very tricky!
snake_img = pygame.image.load("python-files/snake.png")
snake_x = 370
snake_y = 480
snake_x_change = 0
snake_y_change = 0

