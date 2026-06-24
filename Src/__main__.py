#Pygame initialization and operation to display AmbiVi

import pygame
import villager as vil

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
craig.goal = (1270, 700)


# run loop
while running:

    # allows for the game to be exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # clears the previous frame
    screen.fill("white")

    # find desired velocity vector and move

    craig.vel = craig.Seek()
    craig.pos = (craig.pos[0] + craig.vel[0], craig.pos[1] + craig.vel[1])
    pygame.draw.circle(screen, "black", craig.pos, 6)

    # displays any newly rendered items 
    pygame.display.flip()
    

    clock.tick(60)

pygame.quit()
