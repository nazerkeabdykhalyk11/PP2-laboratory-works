import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Display setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels and Timed Food')

# Font setup
font = pygame.font.SysFont("Verdana", 20)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]  # Start length 3
direction = 'RIGHT'
speed = 10
score = 0
level = 1

# Create walls (borders)
walls = []
for x in range(0, WIDTH, CELL_SIZE):
    walls.append((x, 0))
    walls.append((x, HEIGHT - CELL_SIZE))
for y in range(0, HEIGHT, CELL_SIZE):
    walls.append((0, y))
    walls.append((WIDTH - CELL_SIZE, y))

# Generate food with random weight (1–3) and timer (5–10 seconds)
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            weight = random.choice([1, 2, 3])
            timer = random.randint(300, 600)  # ~5–10 seconds at 60 fps
            return (x, y, weight, timer)

# Initialize multiple food items
foods = [generate_food() for _ in range(3)]

# Draw all elements: snake, food, walls, text
def draw_elements():
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw food items
    for food in foods:
        color = RED if food[2] == 1 else YELLOW if food[2] == 2 else WHITE
        pygame.draw.rect(screen, color, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))

    # Score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

# Check collision with self or wall
def check_collision():
    head = snake[0]
    if head in walls or head in snake[1:]:
        return True
    return False

# Game loop
running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arrow keys movement (no reverse allowed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    x, y = snake[0]
    if direction == 'UP': y -= CELL_SIZE
    elif direction == 'DOWN': y += CELL_SIZE
    elif direction == 'LEFT': x -= CELL_SIZE
    elif direction == 'RIGHT': x += CELL_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)

    # Check for food collision
    ate = False
    for food in foods:
        if new_head[0] == food[0] and new_head[1] == food[1]:
            score += food[2]
            foods.remove(food)
            foods.append(generate_food())
            ate = True
            if score % 5 == 0:  # Level up every 5 points
                level += 1
                speed += 2
            break

    if not ate:
        snake.pop()  # Remove tail if not eating

    # Update food timers and remove expired ones
    for food in foods[:]:
        index = foods.index(food)
        new_timer = food[3] - 1
        if new_timer <= 0:
            foods.remove(food)
            foods.append(generate_food())
        else:
            foods[index] = (food[0], food[1], food[2], new_timer)

    # Game over condition
    if check_collision():
        print("Game Over!")
        running = False

    # Draw everything
    draw_elements()
    pygame.display.update()

# Quit game
pygame.quit()
sys.exit()