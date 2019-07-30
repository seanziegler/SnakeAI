import pygame
import random

class Apple:

    def __init__(self):
        self.color = (255,0,0)
        self.size = 32
        self.coordinates = (random.randint(32,768), random.randint(32,368))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size ))


    def eaten(self):
        self.coordinates = (random.randint(32,768), random.randint(32,368))
