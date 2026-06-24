#Pygame initialization and operation to display AmbiVi

import pygame
import villager as vil
import random

# def start
X_BOUNDARY = 1280
Y_BOUNDARY = 720

# init
pygame.init()
screen = pygame.display.set_mode((X_BOUNDARY, Y_BOUNDARY))
clock = pygame.time.Clock()
running = True

# create an actor with a single want
craig = vil.Villager()


# run loop
while running:

    # allows for the game to be exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # clears the previous frame
    screen.fill("white")

    if craig.vel == (0.0, 0.0):
        craig.goal[0] = random.uniform(0, X_BOUNDARY)
        craig.goal[1] = random.uniform(0, Y_BOUNDARY)
    # find desired velocity vector and move
    craig.vel = craig.Seek()
    craig.pos = pygame.Vector2(craig.pos) + craig.vel
    pygame.draw.circle(screen, "black", craig.pos, 6)

    # displays any newly rendered items 
    pygame.display.flip()
    

    clock.tick(60)

pygame.quit()
