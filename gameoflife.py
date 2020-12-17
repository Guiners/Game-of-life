import pygame
import numpy as np
import random as random

pygame.init()

SCREEN_SIZE_Y = 800
SCREEN_SIZE_X = 800

BOARD_HEIGHT = 40
BOARD_WIDTH = 40

PIXEL_SIZE = 20

random.seed(16)
board = np.zeros((BOARD_WIDTH, BOARD_HEIGHT))
gameDisplay = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
clock = pygame.time.Clock()

for i in range(800):
    board[random.randint(0,39), random.randint(0,39)] = round(random.uniform(0,1))



#start population
"""
board[1,0] = 1
board[1,2] = 1
board[0,2] = 1
board[2,1] = 1
board[2,2] = 1
"""
"""
board[0,5] = 1
board[1,5] = 1
board[0,6] = 1
board[1,6] = 1

board[12,9] = 1
board[13,9] = 1
board[11,8] = 1
board[10,7] = 1
board[10,6] = 1
board[10,5] = 1
board[11,4] = 1
board[12,3] = 1
board[13,3] = 1
board[14,6] = 1
board[15,4] = 1
board[15,8] = 1
board[16,6] = 1
board[16,7] = 1
board[16,5] = 1
board[17,6] = 1

board[20,5] = 1
board[20,4] = 1
board[20,3] = 1
board[21,5] = 1
board[21,4] = 1
board[21,3] = 1
board[22,2] = 1
board[22,6] = 1
board[24,2] = 1
board[24,1] = 1
board[24,6] = 1
board[24,7] = 1

board[36,3] = 1
board[36,4] = 1
board[35,3] = 1
board[35,4] = 1
"""



def is_alive(x,y):
    counter_dead = 0
    counter_alive = 0
    try:
        if board[x-1,y-1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x-1,y] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x-1,y+1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x,y-1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x,y+1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x+1,y-1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x+1,y] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass
    try:
        if board[x+1,y+1] == 0:
            counter_dead += 1
        else:
            counter_alive += 1
    except:
        pass

    return counter_alive, counter_dead

while True:

    board2 = np.zeros((BOARD_WIDTH, BOARD_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: exit()

    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if board[i,j] == 0: pygame.draw.rect(gameDisplay, (0,0,0), (i*20, j*20, PIXEL_SIZE, PIXEL_SIZE))
            elif board[i,j] == 1: pygame.draw.rect(gameDisplay, (255,0,255), (i*20, j*20, PIXEL_SIZE, PIXEL_SIZE))

    pygame.display.update()

    for i in range(BOARD_WIDTH):
        for j in range(BOARD_WIDTH):
            alive, dead = is_alive(i,j)
            if board[i,j] == 0 and alive == 3: board2[i,j] = 1
            elif board[i,j] == 1 and alive == 2 or alive == 3: board2[i,j] = 1
            elif board[i,j] == 1 and not alive in [2,3]: board2[i,j] = 0


    board = board2.copy()


    clock.tick(14)
