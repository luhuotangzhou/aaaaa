import pygame
import time
size=width,height =960,641
speed=[-2,1]
# 全屏
# fullsceen=False
# bg=(255,255,255)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("第一个小游戏")
background=pygame.image.load("image/1.jpg").convert()
screen.blit(background,(0,0))
turtle=pygame.image.load('image/4.png')
position=turtle.get_rect()
l_head=turtle
r_head=pygame.transform.flip(turtle,True,False)
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
        if event.type== pygame.KEYDOWN:
            if event.key ==pygame.K_a or event.key==pygame.K_LEFT:
                turtle=r_head
                speed=[-1,0]
            if event.key ==pygame.K_d or event.key==pygame.K_RIGHT:
                turtle=l_head
                speed=[1,0]
            if event.key ==pygame.K_w or event.key==pygame.K_UP:
                speed=[0,-1]
            if event.key ==pygame.K_s or event.key==pygame.K_DOWN:
                speed=[0,1]
            # 全屏(F11)
        #     if event.key==pygame.K_F11:
        #         fullscreen=not fullsceen
        #         if fullsceen:
        #             screen = pygame.display.set_mode((1600,900), FULLSCREEN | HWSURFACE )
        #             width,height=1600,900
        #         else:
        #             screen=pygame.display.set_mode(size)
        # # 用户调整窗口尺寸
        # if event.type==VIDEORESIZE:
        #     size= event.size
        #     width,height=size
        #     print(size)
        #     screen=pygame.display.set_mode(size,RESIZABLE)


# 移动图片
    position=position.move(speed)
    if position.left<0 or position.right>width:
# 翻转图片
        turtle=pygame.transform.flip(turtle,True,False)
#反方向移动
        speed[0]=-speed[0]
    if position.top <0 or position.bottom>height:
        speed[1]=-speed[1]
#填充背景
    screen.blit(background, (0, 0))
    # screen.fill(bg)
#更新图片
    screen.blit(turtle,position)
#更新界面
    pygame.display.flip()
#延迟10 毫秒
    pygame.time.delay(10)
