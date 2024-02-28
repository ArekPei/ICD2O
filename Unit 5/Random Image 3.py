import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Image")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw car body
    pygame.draw.rect(screen, GRAY, (200, 300, 400, 100))
    pygame.draw.rect(screen, GRAY, (250, 250, 300, 50))

    # Draw wheels
    pygame.draw.circle(screen, BLACK, (300, 400), 50)
    pygame.draw.circle(screen, BLACK, (600, 400), 50)

    # Draw windows
    pygame.draw.rect(screen, BLUE, (300, 250, 100, 50))
    pygame.draw.rect(screen, BLUE, (500, 250, 100, 50))

    # Draw headlights
    pygame.draw.circle(screen, WHITE, (325, 325), 20)
    pygame.draw.circle(screen, WHITE, (575, 325), 20)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
