import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Image")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to generate random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw a random shape
def draw_shape(surface):
    shape_type = random.choice(["circle", "rectangle", "polygon"])
    color = random_color()
    if shape_type == "circle":
        radius = random.randint(20, 100)
        x, y = random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius)
        pygame.draw.circle(surface, color, (x, y), radius)
    elif shape_type == "rectangle":
        width, height = random.randint(20, 200), random.randint(20, 200)
        x, y = random.randint(0, WIDTH-width), random.randint(0, HEIGHT-height)
        pygame.draw.rect(surface, color, (x, y, width, height))
    elif shape_type == "polygon":
        num_points = random.randint(3, 8)
        points = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(num_points)]
        pygame.draw.polygon(surface, color, points)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background with gradient
    for y in range(HEIGHT):
        color = (y / HEIGHT * 255, y / HEIGHT * 255, 255)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # Draw shapes
    for _ in range(10):
        draw_shape(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()