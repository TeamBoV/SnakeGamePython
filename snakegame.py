import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Snake")

# Set the background color
bg_color = (0, 0, 0)

# Set the snake's starting position and movement direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the food's starting position
food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
food_spawn = True

# Set the movement direction
direction = 'RIGHT'
change_to = direction

# Set the score to 0
score = 0

# Set the snake's movement speed
clock = pygame.time.Clock()

# Set the font for the score display
font = pygame.font.Font('freesansbold.ttf', 18)

# Set the game over flag to False
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

# If the snake has collided with itself, set the game over flag to True
    if snake_pos in snake_body[1:]:
        game_over = True

    # If the direction is not opposite to the current direction, change the direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Add the new snake head to the snake body
    snake_body.insert(0, list(snake_pos))

    # If the snake has not eaten food, remove the snake's tail
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0] // 10)) * 10, random.randrange(1, (window_size[1] // 10)) * 10]
        food_spawn = True

    # If the snake has collided with the wall or itself, set the game over flag to True
    if snake_pos[0] < 0:
        snake_pos[0] = window_size[0] - 10
    if snake_pos[0] > window_size[0] - 10:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = window_size[1] - 10
    if snake_pos[1] > window_size[1] - 10:
        snake_pos[1] = 0

    # Fill the screen with the background color
    screen.fill(bg_color)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate to 10 FPS
    clock.tick(10)

# Display the game over screen

# Set the font and font size
font = pygame.font.Font('freesansbold.ttf', 32)

# Set the font color to white
font_color = (255, 255, 255)

# Render the "Game Over" text message
game_over_text = font.render("Game Over", True, font_color)

# Get the dimensions of the text message
text_rect = game_over_text.get_rect()

# Set the position of the text message
text_x = screen.get_width() / 2 - text_rect.width / 2
text_y = screen.get_height() / 2 - text_rect.height / 2

# Draw the text message on the screen
screen.blit(game_over_text, [text_x, text_y])

# Update the display
pygame.display.update()

# Wait for the user to close the game window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
