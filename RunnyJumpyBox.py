import pygame
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
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

class RunJumpBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.x_vel = 0
        self.y_vel = 0
        self.jump = 0

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += 1

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_vel -= 5
            if self.x_vel < -20:
                self.x_vel = -20
        if keystate[pygame.K_RIGHT]:
            self.x_vel += 5
            if self.x_vel > 20:
                self.x_vel = 20

        self.x_vel = int(0.8*self.x_vel)

        print(self.rect.left, self.rect.right, self.rect.bottom, self.x_vel, self.y_vel)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.y_vel = 0
            self.jump = 0

        if self.rect.top < 0:
            self.rect.top = 0
            self.y_vel = int(-0.5*self.y_vel)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = RunJumpBox()

all_sprites.add(player)

# Game loop
running = True
while running:
    # Control game speed
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.rect.bottom == HEIGHT:
                    player.y_vel = -15
                    player.jump = 1
                elif player.jump == 1:
                    player.y_vel = -20
                    player.jump = 2
    
    # Update
    all_sprites.update()
    
    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    
pygame.quit()

