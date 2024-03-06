import pygame
import random
import numpy as np

# Initialize pygame
pygame.init()

# Set the screen width and height
screen_width = 800
screen_height = 600

# Set the background color
bg_color = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Armegatron Advanced")

# Create the player 1 bike
player1_bike = pygame.Rect(screen_width / 2, screen_height / 2, 10, 10)

# Set the player 1 bike color
player1_bike_color = (255, 0, 0)

# Set the player 1 bike speed
player1_bike_speed = 10

# Create the player 2 bike
player2_bike = pygame.Rect(screen_width / 2, screen_height / 2, 10, 10)

# Set the player 2 bike color
player2_bike_color = (0, 255, 0)

# Set the player 2 bike speed
player2_bike_speed = 10

# Create the grid
grid = []
for i in range(screen_width // 10):
    for j in range(screen_height // 10):
        grid.append(pygame.Rect(i * 10, j * 10, 10, 10))

# Set the grid color
grid_color = (255, 255, 255)

# Create the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_bike.y -= player1_bike_speed
            elif event.key == pygame.K_DOWN:
                player1_bike.y += player1_bike_speed
            elif event.key == pygame.K_LEFT:
                player1_bike.x -= player1_bike_speed
            elif event.key == pygame.K_RIGHT:
                player1_bike.x += player1_bike_speed

    # Move the player 2 bike
    player2_bike.x += random.randint(-player2_bike_speed, player2_bike_speed)
    player2_bike.y += random.randint(-player2_bike_speed, player2_bike_speed)

    # Check for collisions
    if player1_bike.colliderect(player2_bike):
        running = False

    # Draw the screen
    screen.fill(bg_color)

    # Draw the grid
    for rect in grid:
        pygame.draw.rect(screen, grid_color, rect)

    # Draw the player 1 bike
    pygame.draw.rect(screen, player1_bike_color, player1_bike)

    # Draw the player 2 bike
    pygame.draw.rect(screen, player2_bike_color, player2_bike)

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
