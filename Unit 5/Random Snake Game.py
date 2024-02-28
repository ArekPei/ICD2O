import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.food = self.generate_food()

    def move(self):
        current_head = self.body[0]
        new_head = (current_head[0] + self.direction[0], current_head[1] + self.direction[1])

        if new_head in self.body or not self.is_within_bounds(new_head):
            return False

        self.body.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.body.pop()

        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def generate_food(self):
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        while food in self.body:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        return food

    def is_within_bounds(self, pos):
        return 0 <= pos[0] < GRID_WIDTH and 0 <= pos[1] < GRID_HEIGHT

class Game:
    def __init__(self):
        self.snake = Snake()
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        while True:
            self.handle_events()

            if not self.snake.move():
                print("Game Over! Score:", self.snake.score)
                pygame.quit()
                sys.exit()

            screen.fill(BLACK)

            # Draw snake
            for segment in self.snake.body:
                pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            # Draw food
            pygame.draw.rect(screen, RED, (self.snake.food[0] * GRID_SIZE, self.snake.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()