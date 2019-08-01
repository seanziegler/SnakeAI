import pygame
import random

class Apple:

    def __init__(self):
        self.color = (255,0,0)
        self.size = 1
        self.coordinates = (random.randint(0,100), random.randint(0,100))
        self.rect = pygame.Rect(random.randint(0,100), random.randint(0,100), self.size, self.size)

    def draw(self, screen):
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.size, self.size)
        pygame.draw.rect(screen, self.color, self.rect)

    def eaten(self):
        self.coordinates = (random.randint(0,100), random.randint(0,100))
