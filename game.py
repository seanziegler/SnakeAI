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

        font = pygame.font.SysFont("arial", 18)
        score = 0
        text = font.render('Score: %s' % score, True, (0, 255, 0))

        clock = pygame.time.Clock()
        snake = Snake()
        apple = Apple()

        while running and snake.alive:

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
                    apple.eaten(screen)
                    score += 1

                screen.fill((0,0,0))
                screen.blit(text, (25, 10))
                apple.draw(screen)
                snake.draw(screen)
                clock.tick(4)
                pygame.display.update()

if __name__ == '__main__':
    Game()
