import pygame


#初始化方法
pygame.init()

#创建游戏屏幕宽和高
screen = pygame.display.set_mode((480,700))


#加载游戏背景
bg = pygame.image.load("/home/lzb/images/background.png")
#绘制到屏幕上
screen.blit(bg,(0,0))
#创建英雄
hero = pygame.image.load("/home/lzb/images/life.png")
#绘制到屏幕上
screen.blit(hero,(200,600))


#创建游戏时钟对象
clock = pygame.time.Clock()
#定义英雄的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
while True:
	#设置帧率
	clock.tick(200)
	#更换英雄的位置
	hero_rect.y -=1
	#如果移出屏幕，则回到屏幕底部
	if hero_rect.y+hero_rect.height<=0:
		hero_rect.y = 700
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
	#监听事件
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.KEYDOWN:
			if event.key == 27:
				print("退出游戏")
				#退出
				pygame.quit()
				exit()

