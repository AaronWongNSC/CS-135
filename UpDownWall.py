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

class MovingBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.x_vel = 0
        self.y_vel = 0

    def update(self):
        self.x_vel = 0
        self.y_vel = 0
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_vel = -5
        if keystate[pygame.K_RIGHT]:
            self.x_vel = 5

        self.rect.x += self.x_vel

        collisions = pygame.sprite.spritecollide(self, wall_list, False)
        if collisions:
            if self.x_vel > 0:
                self.rect.right = collisions[0].rect.left
            else:
                self.rect.left = collisions[0].rect.right

        if keystate[pygame.K_UP]:
            self.y_vel = -5
        if keystate[pygame.K_DOWN]:
            self.y_vel = 5
        
        self.rect.y += self.y_vel
        
        collisions = pygame.sprite.spritecollide(self, wall_list, False)
        if collisions:
            if self.y_vel > 0:
                self.rect.bottom = collisions[0].rect.top
            else:
                self.rect.top = collisions[0].rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

class UpDownWall(Wall):
    def __init__(self, x, y, w, h, color, y_min, y_max, up_speed, down_speed):
        Wall.__init__(self, x, y, w, h, color)
        
        self.y_min = y_min
        self.y_max = y_max
        self.up_speed = up_speed
        self.down_speed = down_speed
        
        self.motion = 1
    
    def update(self):
        if self.motion == 1:
            self.rect.y -= self.up_speed
            if self.rect.y < self.y_min:
                self.rect.y = self.y_min
                self.motion *= -1
        else:
            self.rect.y += self.down_speed
            if self.rect.y > self.y_max:
                self.rect.y = self.y_max
                self.motion *= -1

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
goal_sprite = pygame.sprite.Group()

player = MovingBox()

all_sprites.add(player)

wall = Wall((WIDTH/2) - 20, (HEIGHT/2) - 20, 40, 40, RED)
wall_list.add(wall)
all_sprites.add(wall)

wall = UpDownWall(600, 100, 10, 100, GREEN, 100, 400, 5, 5)
wall_list.add(wall)
all_sprites.add(wall)

goal = Wall(700,500, 10, 10, WHITE)
goal_sprite.add(goal)
all_sprites.add(goal)

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
                pass
        
    game_end = pygame.sprite.spritecollide(player, goal_sprite, False)
    print(game_end)
    if game_end:
        running = False

    # Update
    all_sprites.update()

    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    
pygame.quit()
