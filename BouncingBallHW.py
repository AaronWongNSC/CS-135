import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

class BouncingBall(pygame.sprite.Sprite):
    def __init__(self, radius, color, x_vel, y_vel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*radius, 2*radius))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (random.randint(radius, WIDTH - radius), random.randint(radius, HEIGHT - radius))
        self.radius = radius
        
        pygame.draw.circle(self.image, color, [radius,radius], radius)

        self.x_vel = x_vel
        self.y_vel = y_vel
        
    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        
        if self.rect.left < 0:
            self.x_vel *= -1
        if self.rect.right > WIDTH:
            self.x_vel *= -1
        if self.rect.top < 0:
            self.y_vel *= -1
        if self.rect.bottom > HEIGHT:
            self.y_vel *=-1

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
other_balls = pygame.sprite.Group()

mainball = BouncingBall(30, WHITE, 7, 7)

all_sprites.add(mainball)


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
            if event.key == pygame.K_1:
                ball = BouncingBall(40, BLUE, (-1) ** random.randint(0,1) * 5, (-1) ** random.randint(0,1) * 5)
                all_sprites.add(ball)
                other_balls.add(ball)
            if event.key == pygame.K_2:
                ball = BouncingBall(20, RED, (-1) ** random.randint(0,1) * 10, (-1) ** random.randint(0,1) * 10)
                all_sprites.add(ball)
                other_balls.add(ball)


    # Update
    collision = pygame.sprite.spritecollide(mainball, other_balls, True, pygame.sprite.collide_circle)
        
    all_sprites.update()


    # Render
    screen.fill(BLACK) 
    all_sprites.draw(screen)
    pygame.display.flip()
    
pygame.quit()
