import pygame

class Snake:

    ghostPosition = False

    def __init__(self):
        self.length = 1
        self.speed = 20
        self.direction = 'RIGHT'
        self.coordinates = [(400, 300)]
        self.color = (255,255,255)
        self.alive = True

    def eatApple(self):
        self.length += 1
        self.coordinates.append(ghostPosition)


    def move(self):
        self.collideWithWall()
        print(self.coordinates)
        global ghostPosition
        ghostPosition = self.coordinates[-1]
        for index in range(self.length -1, 0, -1):
            self.coordinates[index] = self.coordinates[index  - 1]

        headX, headY = self.coordinates[0]
        if self.direction == 'UP' and self.direction != 'DOWN':
            headY -= self.speed
        if self.direction == 'DOWN' and self.direction != 'UP':
            headY += self.speed
        if self.direction == 'RIGHT' and self.direction != 'LEFT':
            headX += self.speed
        if self.direction == 'LEFT' and self.direction != 'RIGHT':
            headX -= self.speed

        self.coordinates[0] = (headX, headY)
        self.collideWithSnake()



    def collideWithWall(self):
        if self.coordinates[0][0] <= 0 or self.coordinates[0][0] >= 800 or self.coordinates[0][1] <= 0 or self.coordinates[0][1] >= 400:
            self.alive = False

    def collideWithSnake(self):
        if self.coordinates[0] in self.coordinates[1:]:
            self.alive = False

    def draw(self, screen):
        for coordinate in self.coordinates:
            x,y = coordinate
            pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 16, 16 ))
        self.move()
