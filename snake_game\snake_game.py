import pygame
import sys
import random
import time

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.apple = self.generate_apple()

    def generate_apple(self):
        return (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

    def draw_snake(self):
        for pos in self.snake:
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def draw_apple(self):
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.apple[0], self.apple[1], BLOCK_SIZE, BLOCK_SIZE))

    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)
        self.snake.insert(0, new_head)

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            return True
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            self.move_snake()
            if self.snake[0] == self.apple:
                self.apple = self.generate_apple()
            else:
                self.snake.pop()

            self.screen.fill(BLACK)
            self.draw_snake()
            self.draw_apple()
            pygame.display.flip()

            if self.check_collision():
                print("Game Over")
                pygame.quit()
                sys.exit()

            self.clock.tick(SPEED)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()