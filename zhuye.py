import pygame
speed=[-2,1]
# 设置窗口大小
size=width,height =1024,768
screen=pygame.display.set_mode(size)
# 设置背景主题
pygame.display.set_caption("打靶小游戏")
# 设置背景图片
background=pygame.image.load("image/bg_game.jpg").convert()
screen.blit(background,(0,0))
background1=pygame.image.load("image/grass.png")
screen.blit(background1,(0,387))
background2=pygame.image.load("image/tree.png")
screen.blit(background2,(0,235))
background3=pygame.image.load("image/but_exit.png")
screen.blit(background3,(960,0))
# 加入瞄准器
turtle=pygame.image.load('image/gun_sight.png')
position=turtle.get_rect()
# moving=False
while True:
    screen.blit(background, (0, 0))
    screen.blit(background1, (0, 387))
    screen.blit(background2, (0,235))
    screen.blit(background3, (960, 0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #             # 1鼠标左边2鼠标中间3鼠标右边4滚轮往上5滚轮往下
    #         if event.button == 1:
    #             moving = True
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         if event.button == 1:
    #             moving == False
    # if moving:
    #         # 获得鼠标在干嘛
    #     position = pygame.mouse.get_pos()
        elif event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_a or event.key==pygame.K_LEFT:
                speed = [-3, 0]
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                speed = [3, 0]
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                speed = [0, -3]
            if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                speed = [0, 3]
    # 移动图片
    position = position.move(speed)
    print(position)
    if position.left < 0 or position.right > width:
    #     # 翻转图片
    #     # turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    # 更新图片
    screen.blit(turtle, position)
     # 更新界面
    pygame.display.flip()
    # 延迟10 毫秒
    pygame.time.delay(5)
    pygame.display.update()