import pygame
pygame.init()

# параметры окна: размер, название, цвет фона
window_size = (800, 600) 
screen = pygame.display.set_mode(window_size) 
pygame.display.set_caption("Draw circle")
ball_color = pygame.Color('red')  # цвет шара
bg_color = pygame.Color('white')  # цвет фона

ball_pos = [400, 300]  # начальная позиция шара

ball_radius = 25  # радиус шара

speed = 20  # скорость движения шара

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()  # получение всех нажатий клавиш
    if keys[pygame.K_UP]: 
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)  # движение вверх
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, window_size[1] - ball_radius)  # движение вниз
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)  # движение влево
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, window_size[0] - ball_radius)  # движение вправо
    
    screen.fill(bg_color)  # очистка экрана
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)  # отрисовка шара
    pygame.display.flip()  # обновление экрана
    pygame.time.Clock().tick(24)  # ограничение FPS
