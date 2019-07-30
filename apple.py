import pygame

class Apple:

    def __init__(self):
        self.color = (255,0,0)
        self.size = 8
        self.coordinates = (250, 400)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size ))
