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

class BouncingBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.x_vel = 5
        self.y_vel = 5

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        if self.rect.right > WIDTH:
            self.x_vel = -5
        if self.rect.left < 0:
            self.x_vel = 5
        if self.rect.top < 0:
            self.y_vel = 5
        if self.rect.bottom > HEIGHT:
            self.y_vel = -5

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

newbbox = BouncingBox()

all_sprites.add(newbbox)

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
    all_sprites.update()
    
    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    
pygame.quit()

