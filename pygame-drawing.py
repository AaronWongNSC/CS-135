import pygame
import random
import math

# Constants
WIDTH = 360
HEIGHT = 480
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Control game speed
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    
    # Render
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, WHITE, [10, 10, 20, 30])

    pygame.draw.polygon(screen, RED, [[50,10], [50,40], [70,15]])

    pygame.draw.polygon(screen, RED,
                        [[10,50], [15,70], [20,50], [10,70], [15,50], [20,70]])

    pygame.draw.circle(screen, BLUE, [80,20], 10)

    pygame.draw.ellipse(screen, GREEN, [10, 10, 20, 30])

    pygame.draw.arc(screen, GREEN, [50, 50, 20, 30], 0, math.pi/2)

    pygame.draw.line(screen, CYAN, [100,100], [100,200])
    
    pygame.draw.lines(screen, YELLOW, False, [[100,300], [150,350], [100,400]])

    pygame.display.flip()
    
pygame.quit()
