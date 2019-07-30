import pygame

class Snake:

    ghostPosition = False

    def __init__(self):
        self.length = 1
        self.speed = 4
        self.direction = 'RIGHT'
        self.coordinates = [(50, 50)]
        self.color = (255,255,255)

    def eatApple(self):
        self.length += 1
        self.coordinates.append(ghostPosition)



    def move(self):
        global ghostPosition
        ghostPosition = self.coordinates[-1]
        print(ghostPosition)
        for index in range(0, self.length - 1):
            self.coordinates[index + 1] = (self.coordinates[index])

        headX, headY = self.coordinates[0]
        if self.direction == "UP":
            headY -= self.speed
        if self.direction == "DOWN":
            headY += self.speed
        if self.direction == "RIGHT":
            headX += self.speed
        if self.direction == "LEFT":
            headX -= self.speed

        self.coordinates[0] = (headX, headY)

        print(self.coordinates)

    def die(self):
        pass


    def draw(self, screen):
        for coordinate in self.coordinates:
            x,y = coordinate
            #print(self.coordinates[0])
            pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 8, 8 ))
        self.move()
