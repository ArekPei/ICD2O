import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Colors
SKY_BLUE = (135, 206, 235)
SUN_YELLOW = (255, 215, 0)
GRASS_GREEN = (34, 139, 34)
TREE_BROWN = (139, 69, 19)
HOUSE_BASE_COLOR = (240, 128, 128)
ROOF_COLOR = (178, 34, 34)
WINDOW_COLOR = (176, 224, 230)
DOOR_COLOR = (160, 82, 45)
MOUNTAIN_COLOR = (128, 128, 128)
SNOW_COLOR = (255, 250, 250)
FENCE_COLOR = (139, 69, 19)
BRIDGE_COLOR = (139, 69, 19)
RIVER_BLUE = (70, 130, 180)

class Scene:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Artistic Scene")

    def draw_background(self):
        self.screen.fill(SKY_BLUE)

    def draw_shapes(self):
        # Drawing a sun
        pygame.draw.circle(self.screen, SUN_YELLOW, (700, 100), 80)

        # Drawing mountains
        pygame.draw.polygon(self.screen, MOUNTAIN_COLOR, [(0, 400), (200, 100), (400, 400)])
        pygame.draw.polygon(self.screen, SNOW_COLOR, [(200, 100), (300, 50), (250, 100)])

        # Drawing grass
        pygame.draw.rect(self.screen, GRASS_GREEN, (0, 400, SCREEN_WIDTH, SCREEN_HEIGHT))

        # Drawing trees
        self.draw_tree(100, 380)
        self.draw_tree(200, 380)
        self.draw_tree(300, 380)
        self.draw_tree(500, 380)
        self.draw_tree(600, 380)

        # Drawing a house
        self.draw_house(550, 320)

        # Drawing a fence
        self.draw_fence(50, 450, 500)

        # Drawing a river
        pygame.draw.rect(self.screen, RIVER_BLUE, (0, 480, SCREEN_WIDTH, 120))

        # Drawing a bridge
        self.draw_bridge(200, 470, 400, 100, 60)

    def draw_tree(self, x, y):
        pygame.draw.rect(self.screen, TREE_BROWN, (x + 15, y + 60, 20, 40))
        pygame.draw.polygon(self.screen, GRASS_GREEN, [(x, y + 40), (x + 50, y + 40), (x + 25, y)])
        pygame.draw.polygon(self.screen, GRASS_GREEN, [(x - 10, y + 20), (x + 60, y + 20), (x + 25, y - 40)])

    def draw_house(self, x, y):
        pygame.draw.rect(self.screen, HOUSE_BASE_COLOR, (x, y, 200, 150))
        pygame.draw.polygon(self.screen, ROOF_COLOR, [(x, y), (x + 100, y - 100), (x + 200, y)])
        pygame.draw.rect(self.screen, WINDOW_COLOR, (x + 40, y + 40, 50, 50))
        pygame.draw.rect(self.screen, WINDOW_COLOR, (x + 110, y + 40, 50, 50))
        pygame.draw.rect(self.screen, DOOR_COLOR, (x + 85, y + 80, 30, 70))

    def draw_fence(self, x, y, length):
        pygame.draw.line(self.screen, FENCE_COLOR, (x, y), (length, y), 5)

    def draw_bridge(self, x, y, width, radius, gap):
        pygame.draw.arc(self.screen, BRIDGE_COLOR, (x, y - radius, width, 2 * radius), 0, 3.14, 10)
        pygame.draw.arc(self.screen, BRIDGE_COLOR, (x, y - radius - gap, width, 2 * radius), 0, 3.14, 10)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_background()
            self.draw_shapes()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    scene = Scene()
    scene.run()