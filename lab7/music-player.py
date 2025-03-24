import pygame
import os

pygame.init()

playlist = []
# путь к папке с музыкой
music_folder = "/Users/erkeabdykhalyk/pp2/pp2 labs/lab7/musics"
allmusic = os.listdir(music_folder)

# добавляем в плейлист только файлы с расширением .mp3
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

# параметры окна: размер и заголовок
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Playlist")
clock = pygame.time.Clock()

# загружаем фон
background = pygame.image.load(os.path.join("images", "background.png"))

# создаем область для кнопок, задаем цвет (белый)
bg = pygame.Surface((500, 170))
bg.fill((255, 255, 255))

# шрифт для отображения названия трека
font2 = pygame.font.SysFont(None, 20)

# загружаем кнопки
playb = pygame.image.load(os.path.join("images", "play.png"))
pausb = pygame.image.load(os.path.join("images", "pause.png"))
nextb = pygame.image.load(os.path.join("images", "next.png"))
prevb = pygame.image.load(os.path.join("images", "back.png"))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:  # при нажатии клавиши
            if event.key == pygame.K_SPACE:  # если нажата пробел
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:  # если нажата стрелка вправо
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:  # если нажата стрелка влево
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    
    # отображение названия текущего трека
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    
    # расположение кнопок и фона
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
