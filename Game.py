import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 800
BG_COLOR = (50, 150, 255)  # Blue background
BUBBLE_COLOR = (255, 255, 255)  # White bubbles
CATCHER_COLOR = (200, 50, 50)  # Red catcher

# Bubble settings
BUBBLE_RADIUS = 20
BUBBLE_SPEED = 4
BUBBLE_SPAWN_RATE = 60  # Lower is faster spawning

# Catcher settings
CATCHER_WIDTH = 100
CATCHER_HEIGHT = 20
CATCHER_SPEED = 8

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Catch Game")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Game variables
bubbles = []
catcher_x = WIDTH // 2 - CATCHER_WIDTH // 2
score = 0
game_over = False
frame_count = 0

# Game Loop
running = True
while running:
    screen.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move catcher
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and catcher_x > 0:
        catcher_x -= CATCHER_SPEED
    if keys[pygame.K_RIGHT] and catcher_x < WIDTH - CATCHER_WIDTH:
        catcher_x += CATCHER_SPEED
    
    # Spawn bubbles
    frame_count += 1
    if frame_count % BUBBLE_SPAWN_RATE == 0:
        bubble_x = random.randint(BUBBLE_RADIUS, WIDTH - BUBBLE_RADIUS)
        bubbles.append([bubble_x, 0])
    
    # Move bubbles and check for catching
    new_bubbles = []
    for bubble in bubbles:
        bubble[1] += BUBBLE_SPEED  # Move down
        if bubble[1] < HEIGHT - CATCHER_HEIGHT or (catcher_x < bubble[0] < catcher_x + CATCHER_WIDTH and bubble[1] >= HEIGHT - CATCHER_HEIGHT):
            new_bubbles.append(bubble)
            pygame.draw.circle(screen, BUBBLE_COLOR, (bubble[0], bubble[1]), BUBBLE_RADIUS)
        else:
            if bubble[1] >= HEIGHT - CATCHER_HEIGHT:
                game_over = True
    bubbles = new_bubbles
    
    # Draw catcher
    pygame.draw.rect(screen, CATCHER_COLOR, (catcher_x, HEIGHT - CATCHER_HEIGHT, CATCHER_WIDTH, CATCHER_HEIGHT))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # Check game over
    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(30)
    
    # Restart game
    if game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            bubbles = []
            score = 0
            game_over = False

pygame.quit()
