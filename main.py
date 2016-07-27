import pygame
from pygame.locals import *
from game import Game
import random

# Enter maximum resolution of game window
max_width = 800
max_height = 600

# Enter matrix size
n = 10  # height
# m = 10  # width
m = n

# Scale game window to fit grid nicely (so that each cell is a perfect square, not stretched)
if max_width*n >= max_height*m:
    height = max_height
    width = (m*max_height)/n
else:
    width = max_width
    height = (n*max_width)/m

tile_width = width/m
tile_height = height/n

# Setup pygame screen
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dots')

background = pygame.Surface(screen.get_size())
background = background.convert()

# Load tile images
empty = pygame.image.load('empty.png')
white = pygame.image.load('white.png')
black = pygame.image.load('black.png')

def draw(board):
    n = len(board)
    m = len(board[0])
    for i in xrange(n):
        for j in xrange(m):
            tile = empty
            if board[i][j] == 1:
                tile = white
            elif board[i][j] == 2:
                tile = black
            screen.blit(tile, (j * width / m, i * height / n))
    pygame.display.flip()

# Can use smoothing here. Smoothed tiles look more aesthetic, but perhaps not pixel-precise
empty = pygame.transform.smoothscale(empty, (width/m, height/n))
white = pygame.transform.smoothscale(white, (width/m, height/n))
black = pygame.transform.smoothscale(black, (width/m, height/n))

game = Game(n)
draw(game.get_board())

# Flip display
# pygame.display.flip()

# This loop waits for mouse clicks and handles them
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pass
                # print "Left mouse click"
            elif pygame.mouse.get_pressed()[2]:
                pass
                # print "Right mouse click"
            x, y = pygame.mouse.get_pos()
            i, j = y/tile_height, x/tile_width
            print "Coordinates of tile: %d %d" % (i, j)
            # Do whatever you want with these coordinates!
            game.put_counter(i, j)
            draw(game.get_board())

print "Program terminated."