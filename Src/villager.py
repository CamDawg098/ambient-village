import pygame


VILLAGER_BASE_SPEED = 10

class Villager:
    """ A individualized actor """

    def __init__(self, name = "Craig"):
        self.name = name
        self.speed = VILLAGER_BASE_SPEED
        self.vel = pygame.Vector2()
        self.pos = pygame.Vector2()
        self.goal = pygame.Vector2()

    def Seek(self):
        desired = pygame.math.Vector2((self.goal[0] - self.pos[0], self.goal[1] - self.pos[1]))
        d = desired.length()
        if d < 1:
            desired = pygame.Vector2()
        elif d < 100:
            m = min((d/100) * self.speed, self.speed)
            desired.scale_to_length(m)
        else:
            desired.scale_to_length(self.speed)
        return desired

