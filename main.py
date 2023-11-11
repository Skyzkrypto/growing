
import pygame
pygame.init()

import random

run = True

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Snake Game")

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.X = 50
        self.Y = 50
        self.velocity = 1
        self.image = pygame.image.load('../assets/player.png')
        self.image = pygame.transform.scale(self.image, (self.X, self.Y))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def move_top(self):
        self.rect.y -= self.velocity

    def move_bottom(self):
        self.rect.y += self.velocity

    def grow(self):

        # Size
        self.X = self.X + 5
        self.Y = self.Y + 5

        # Speed
        self.velocity = self.velocity + 0.1

        # Screen refresh
        self.image = pygame.transform.scale(self.image, (self.X, self.Y))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 450

        print("Size : " and self.X)
        print("Velocity : " and self.velocity)
        print("Growing...")

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('../assets/food.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 450


# Player
player = Player()

# Food
food = Food()

while run:

    # Collisions
    if player.rect.colliderect(food.rect):
        player.grow()
        
        food.rect.x = random.randint(0, 1030)
        food.rect.y = random.randint(0, 670)

    # Destruction
    if player.rect.x == 1080:
        run = False
        print('Game over')
    elif player.rect.x == 0:
        run = False
        print('Game over')
    elif player.rect.y == 720:
        run = False
        print('Game over')
    elif player.rect.y == 0:
        run = False
        print('Game over')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_top()
    if keys[pygame.K_DOWN]:
        player.move_bottom()

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(food.image, food.rect)
    pygame.display.update()

pygame.quit(
