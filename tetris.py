import pygame
import random
#game window size
screen_width=1080
screen_height=720
block_size=120
board_width=screen_width//block_size
board_height=screen_height//block_size
#increase game
fsp=20
shape = [
    [[1,1,1,1]],#i
    [[1,1], [1,1]], #O
    [[1,1,0], [0,1,1]], #s
    [[0,1,1], [0,1,1]], #z
    [[1,1,1], [0,1,0]], #l
    [[1,1,1], [0,0,1]] #J


]
COLOR = [
    (0, 255, 255), #cyan
    (255, 255, 0), #yellow
    (0, 255, 0), #green
    (255, 0, 0), #red
    (255, 0, 255), #Magenta
    (255, 165, 0), #Orange
    (0,0, 255) #Blue
]


class Game_tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = [[0]* board_width for _ in range (board_height)]
        self.gameover = False



