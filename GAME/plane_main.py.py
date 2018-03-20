import pygame
from plane_sprites import *
HERO_FIRE_EVENT = pygame.USEREVENT+1

#音乐
pygame.init()
pygame.mixer.music.load("/home/lzb/images/Alan Walker - Sky.mp3")
pygame.mixer.music.play(loops=-1)
#游戏框架
class PlaneGame(object):
	#初始化游戏数据
	def __init__(self):
		#创建游戏窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		#游戏时钟
		self.clock = pygame.time.Clock()
		#创建精灵和精灵组
		self.__create_sprites()
		pygame.display.set_caption("灰机大战")
		#设置一个定时器事件  每一秒钟创建一架敌机
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 200)
		#子弹发射速度
		pygame.time.set_timer(HERO_FIRE_EVENT, 400)
	#开始游戏
	def start_game(self):
		while True:
			#1.刷新帧率
			self.clock.tick(200)
			#2.监听事件
			self.__handler_event()
			#3.碰撞检测b
			self.__check_collide()
			#4.更新精灵和精灵组
			self.__update_sprites()
			#5.刷新屏幕
			pygame.display.update()
	#创建精灵和精灵组
	def __create_sprites(self):

		bg1 = Background()
		bg2 = Background(True)
		self.hero = Hero()
		self.hero2 = Hero_Two()
		#英雄精灵组
		self.hero_group = pygame.sprite.Group(self.hero,self.hero2)
		#背景精灵组#调用父类的方法 让敌机在水平方向运动
		self.bg_group = pygame.sprite.Group(bg1,bg2)
		#敌机精灵组
		self.diji_group = pygame.sprite.Group()

	#监听事件
	def __handler_event(self):
		for event in pygame.event.get():
			keys_pressed = pygame.key.get_pressed()
			
			#控制飞机移动
			if keys_pressed[276]:
				self.hero.move = False
				self.hero.speed = -10
			elif keys_pressed[275]:
				self.hero.move = False
				self.hero.speed = 10
			elif keys_pressed[273]:
				self.hero.move = True
				self.hero.speed = -10
			elif keys_pressed[274]:
				self.hero.move = True
				self.hero.speed = 10
			else:
				self.hero.speed = 0


			if keys_pressed[97]:
				self.hero2.Move = False
				self.hero2.speed = -10
			elif keys_pressed[100]:
				self.hero2.Move = False
				self.hero2.speed = 10
			elif keys_pressed[119]:
				self.hero2.Move = True
				self.hero2.speed = -10
			elif keys_pressed[115]:
				self.hero2.Move = True
				self.hero2.speed = 10
			else:
				self.hero2.speed = 0
			#退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			#将敌机添加到精灵组里
			elif event.type == CREATE_ENEMY_EVENT:
				self.diji_group.add(Enemy())
			#英雄发子弹
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				self.hero2.fire()
				
	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()

	#碰撞检测
	def __check_collide(self):
		#子弹销毁敌机
		pygame.sprite.groupcollide(self.hero.bullets_group,self.diji_group,True,True)
		pygame.sprite.groupcollide(self.hero2.bullet_group,self.diji_group,True,True)
		#敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.diji_group,True)
		enemie = pygame.sprite.spritecollide(self.hero2,self.diji_group,True)
		#判断列表时候有内容
		if len(enemies) > 0:
			self.hero.kill()
			self.hero.rect.y = -10000
		if len(enemie) > 0:
			self.hero2.kill()
			self.hero2.rect.y = -10000
		#判断两个敌机都死亡退出游戏
		if self.hero.rect.y == -10000 and self.hero2.rect.y == -10000:
			self.__game_over()
	#更新精灵和精灵组
	def __update_sprites(self):
		# self.hero_group.update()
		# self.hero_group.draw()

		# self.diji_group.update()
		# self.diji_group.draw()

		# self.bg_group.update()
		# self.bg_group.draw()
		for a in [self.bg_group,self.diji_group,self.hero_group,self.hero.bullets_group,self.hero2.bullet_group]:
			a.update()
			a.draw(self.screen)


if __name__ == "__main__":
	#使用游戏类创建游戏对象
	game = PlaneGame()

	#开始游戏
	game.start_game()