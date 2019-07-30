import pygame
from snake import Snake
from apple import Apple

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('SnakeAI')
        screen = pygame.display.set_mode((800,600))
        self.run(screen)


    def run(self, screen):
        running = True
        clock = pygame.time.Clock()
        snake = Snake()
        apple = Apple()


        while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            snake.direction = 'UP'
                        if event.key == pygame.K_DOWN:
                            snake.direction = 'DOWN'
                        if event.key == pygame.K_RIGHT:
                            snake.direction = 'RIGHT'
                        if event.key == pygame.K_LEFT:
                            snake.direction = 'LEFT'
                        if event.key == pygame.K_SPACE:
                            snake.eatApple()
                pygame.event.clear()
                
                if apple.coordinates == snake.coordinates:
                    snake.eatApple()


                screen.fill((0,0,0))
                snake.draw(screen)
                apple.draw(screen)
                clock.tick(1)
                pygame.display.update()

if __name__ == '__main__':
    Game()
