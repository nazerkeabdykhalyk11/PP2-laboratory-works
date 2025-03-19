import pygame 
import time
import math
pygame.init()

# параметры появляющегося окна
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# название в верхней части окна
pygame.display.set_caption("Mickey's clock")

# внесение картинок в окно
leftarm = pygame.image.load("images/leftarm.png")
rightarm = pygame.image.load("images/rightarm.png")
mainclock = pygame.transform.scale(pygame.image.load("images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # с помощью localtime определяем минуты и секунды
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # определяем градусы минут и секунд
    # текущая минута * 360 градусов / 60 минут + текущая секунда 
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
    # добавляем фон на экран
    screen.blit(mainclock, (0,0))
    
    # правая рука - стрелка минут
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    # левая рука - стрелка секунд
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() # обновляет окно
    clock.tick(60) # FPS
    
pygame.quit()