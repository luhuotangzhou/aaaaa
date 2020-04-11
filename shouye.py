import pygame
import sys
from pygame.locals import*
# 初始化
pygame.init()
pygame.mixer.init()
# 设置窗口大小
size=width,height =1024,768
screen=pygame.display.set_mode(size)
# 设置背景主题
pygame.display.set_caption("打靶小游戏")
background=pygame.image.load("image/shouye.png").convert()
screen.blit(background,(0,0))
background1=pygame.image.load("image/play.png")
screen.blit(background1,(500,500))
# 添加背景音乐
pygame.mixer.music.load("image/ds_soundtrack.ogg")
# 设置声音大小
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

pause=False
pause_image=pygame.image.load("image/audio_icon.png").convert_alpha()
unpause_image=pygame.image.load("image/audio_uicon.png").convert_alpha()

clock=pygame.time.Clock()
while True:
    screen.blit(background, (0, 0))
    screen.blit(background1, (400, 550))
    # screen.blit(pasue_image, (0, 0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()

        if event.type==MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            if event.button == 1 and x1>=940 and x1<=1024 and 0<=y1<=80:
                pause=not pause
            elif event.button ==1 and 500<=x1<=729  and 500<=y1<=626:
                pass

    if pause:
        screen.blit(pause_image,(940,0))
        # 配置声音
        pygame.mixer.music.unpause()
    else:
        screen.blit(unpause_image,(940,0))
        pygame.mixer.music.pause()

    pygame.display.update()
    clock.tick(30)