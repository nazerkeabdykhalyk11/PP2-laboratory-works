import pygame
import random
import sys
import psycopg2  # ← добавили PostgreSQL

# PostgreSQL setup
conn = psycopg2.connect(
    dbname="snake game",  # или postgres, если ты в ней работаешь
    user="postgres",
    password="erketaika11",  # ← замени на свой
    host="localhost"
)
cur = conn.cursor()

# User login
username = input("Enter your username: ")
cur.execute("SELECT id, level FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id, level = user
    print(f"Welcome back, {username}! Current level: {level}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    level = 1
    print(f"Welcome, new player {username}!")

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
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
speed = 10 + (level - 1) * 2  # базовая скорость + от уровня
score = 0

# Walls
walls = []
for x in range(0, WIDTH, CELL_SIZE):
    walls.append((x, 0))
    walls.append((x, HEIGHT - CELL_SIZE))
for y in range(0, HEIGHT, CELL_SIZE):
    walls.append((0, y))
    walls.append((WIDTH - CELL_SIZE, y))

# Food
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            weight = random.choice([1, 2, 3])
            timer = random.randint(300, 600)
            return (x, y, weight, timer)

foods = [generate_food() for _ in range(3)]

def draw_elements():
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    for food in foods:
        color = RED if food[2] == 1 else YELLOW if food[2] == 2 else WHITE
        pygame.draw.rect(screen, color, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
    for wall in walls:
        pygame.draw.rect(screen, BLUE, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

def check_collision():
    head = snake[0]
    return head in walls or head in snake[1:]

# Main loop
running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    elif keys[pygame.K_p]:  # P = Pause and Save
        cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
        conn.commit()
        print("Game paused & score saved!")
        running = False

    # Move snake
    x, y = snake[0]
    if direction == 'UP': y -= CELL_SIZE
    elif direction == 'DOWN': y += CELL_SIZE
    elif direction == 'LEFT': x -= CELL_SIZE
    elif direction == 'RIGHT': x += CELL_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)

    ate = False
    for food in foods:
        if new_head[0] == food[0] and new_head[1] == food[1]:
            score += food[2]
            foods.remove(food)
            foods.append(generate_food())
            ate = True
            if score % 5 == 0:
                level += 1
                speed += 2
            break

    if not ate:
        snake.pop()

    for food in foods[:]:
        index = foods.index(food)
        new_timer = food[3] - 1
        if new_timer <= 0:
            foods.remove(food)
            foods.append(generate_food())
        else:
            foods[index] = (food[0], food[1], food[2], new_timer)

    if check_collision():
        print("Game Over!")
        cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
        conn.commit()
        running = False

    draw_elements()
    pygame.display.update()

pygame.quit()
cur.close()
conn.close()
sys.exit()
