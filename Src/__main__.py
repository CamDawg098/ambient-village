#Pygame initialization and operation to display AmbiVi

import pygame

# initialize Pygame background things
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    # allows for the game to be exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # clears the previous frame
    screen.fill("white")

    pygame.draw.circle(screen, "blue", ((640, 360)), 15)

    # displays any newly rendered items 
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
