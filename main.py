# write a python 2d game with pygame for soccer with 2 players, one computer controlled. The field is green and 800x600 pixels, the goals are yellow on both right and left sides. The players are red and blue. There is a black and white ball and the goal of the game is for a player to send the ball into the yellow goals. ﻿```python
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Soccer")

# Set the background color
screen.fill((0, 128, 0))

# Define the players' colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the players
player1 = pygame.sprite.Sprite()
player1.image = pygame.Surface((30, 60))
player1.image.fill(RED)
player1.rect = player1.image.get_rect()
player1.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

player2 = pygame.sprite.Sprite()
player2.image = pygame.Surface((30, 60))
player2.image.fill(BLUE)
player2.rect = player2.image.get_rect()
player2.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create the ball
ball = pygame.sprite.Sprite()
ball.image = pygame.Surface((25, 25))
ball.image.fill((0, 0, 0))
ball.rect = ball.image.get_rect()
ball.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
ball.speed_x = 2
ball.speed_y = 2 

# Create the goals
goal1 = pygame.sprite.Sprite()
goal1.image = pygame.Surface((20, 140))
goal1.image.fill((255, 255, 0))
goal1.rect = goal1.image.get_rect()
goal1.rect.center = (0, SCREEN_HEIGHT / 2)

goal2 = pygame.sprite.Sprite()
goal2.image = pygame.Surface((20, 140))
goal2.image.fill((255, 255, 0))
goal2.rect = goal2.image.get_rect()
goal2.rect.center = (SCREEN_WIDTH, SCREEN_HEIGHT / 2)

# Create a group to hold all the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)
all_sprites.add(goal1)
all_sprites.add(goal2)

# Set the game loop flag
running = True

# Set the clock
clock = pygame.time.Clock()

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player's position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player1.rect.y += 5
    if keys[pygame.K_LEFT]:
        player1.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player1.rect.x += 5

    # Update the computer player's position
    if ball.rect.centerx < SCREEN_WIDTH / 2:
        player2.rect.x = ball.rect.centerx - 30
    else:
        player2.rect.x = ball.rect.centerx + 30

    # Keep the player within the screen
    if player1.rect.left < 0:
        player1.rect.left = 0
    if player1.rect.right > SCREEN_WIDTH:
        player1.rect.right = SCREEN_WIDTH
    if player1.rect.top < 0:
        player1.rect.top = 0
    if player1.rect.bottom > SCREEN_HEIGHT:
        player1.rect.bottom = SCREEN_HEIGHT

    # Keep the computer player within the screen
    if player2.rect.left < 0:
        player2.rect.left = 0
    if player2.rect.right > SCREEN_WIDTH:
        player2.rect.right = SCREEN_WIDTH
    if player2.rect.top < 0:
        player2.rect.top = 0
    if player2.rect.bottom > SCREEN_HEIGHT:
        player2.rect.bottom = SCREEN_HEIGHT

    # Update the ball's position
    ball.rect.x += ball.speed_x
    ball.rect.y += ball.speed_y

    # Keep the ball within the screen
    if ball.rect.left < 0 or ball.rect.right > SCREEN_WIDTH:
        ball.speed_x *= -1
    if ball.rect.top < 0 or ball.rect.bottom > SCREEN_HEIGHT:
        ball.speed_y *= -1

    # Check for collisions between the ball and the players
    if pygame.sprite.collide_rect(ball, player1):
        ball.speed_x *= -1
    if pygame.sprite.collide_rect(ball, player2):
        ball.speed_x *= -1

    # Check for a goal
    if ball.rect.colliderect(goal1.rect):
        print("Player 2 (red) wins!")
        running = False
    if ball.rect.colliderect(goal2.rect):
        print("Player 1 (blue) wins!")
        running = False

    # Update the display
    screen.fill((0, 128, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()