import pygame

VILLAGER_BASE_SPEED = 10

class Villager:
    """ A individualized actor """

    def __init__(self, name = "Craig"):
        self.name = name
        self.speed = VILLAGER_BASE_SPEED
        self.vel = (0, 0)
        self.pos = (0, 0)
        self.goal_pos = (0, 0)


