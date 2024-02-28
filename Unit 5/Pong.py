import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, direction):
        self.rect.y += direction * PADDLE_SPEED
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dx = -self.dx

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class PongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.paddle1 = Paddle(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle2 = Paddle(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle1.move(-1)
        if keys[pygame.K_RIGHT]:
            self.paddle1.move(1)
        if keys[pygame.K_UP]:
            self.paddle2.move(-1)
        if keys[pygame.K_DOWN]:
            self.paddle2.move(1)

        self.ball.move()
        self.ball.check_collision(self.paddle1)
        self.ball.check_collision(self.paddle2)

        if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.rect.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            self.ball.rect.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            self.ball.dx = -self.ball.dx

    def draw(self):
        self.screen.fill(BLACK)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.draw.line(self.screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 2)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    game = PongGame()
    game.run()