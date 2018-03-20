import pygame
import random
#定时器常量 
CREATE_ENEMY_EVENT = pygame.USEREVENT

SCREEN_RECT = pygame.Rect(0, 0, 1300, 700)

class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_url,new_speed=1):
		super().__init__()
		self.image = pygame.image.load(image_url)
		self.rect = self.image.get_rect()
		self.speed = new_speed

	def update(self,*args):
		#默认水平方向移动
		self.rect.x -= self.speed

#游戏背景精灵
class Background(GameSprite):
	def __init__(self,is_alt=False):
		super().__init__("/home/lzb/images/yyy.png",1)

		if is_alt:
			self.rect.left = self.rect.width
	def update(self):
		self.rect.x -= self.speed
		#判断是否移出屏幕 如果移出 将图像设置到屏幕右方
		if self.rect.x <=  -self.rect.width:
			self.rect.left = self.rect.width

#敌机精灵
class Enemy(GameSprite):
	def __init__(self):

		super().__init__("/home/lzb/images/enemy1.png")
		#随机速度
		self.speed = random.randint(5, 15)
		#设置敌机的初始位置
		self.rect.x = SCREEN_RECT.width + self.rect.width
		max_ = SCREEN_RECT.height -self.rect.height
		self.rect.y = random.randint(0, max_)

	def update(self):
		
		# panduan = random.randint(0, 2)
		# if panduan == 0:
		# 	self.rect.y -= self.speed
		# 	self.rect.x -= self.speed
		# elif panduan == 1:
		# 	self.rect.y += self.speed
		# 	self.rect.x -= self.speed
		# elif panduan == 2:
		self.rect.x -= self.speed
		#判断敌机是否飞出屏幕  如果飞出屏幕将敌机从精灵组删除
		if self.rect.right <=0 :
			self.kill()



#英雄精灵
class Hero(GameSprite):

	def __init__(self):
		super().__init__("/home/lzb/images/me1.png")

		#初始位置
		self.rect.centery = SCREEN_RECT.centery+100
		self.rect.left = SCREEN_RECT.y-20
		self.move = True
		#子弹精灵组
		self.bullets_group = pygame.sprite.Group()
	def update(self):
		#super().update()

		#控制飞机移动
		if not self.move:
			self.rect.x += self.speed
		else:
			self.rect.y += self.speed

		#飞机飞出屏幕
		if self.rect.bottom <= 0:
		 	self.rect.y = self.rect.bottom+SCREEN_RECT.height
		elif self.rect.y >= SCREEN_RECT.height:
		 	self.rect.y = -self.rect.height

		if self.rect.x <= 0:
			self.rect.x = 0
		elif self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width
	def fire(self):
		for i in (1,2,3):
			#创建子弹精灵
			bullet1 = Bullet()
			bullet2 = Bullet()
			bullet3 = Bullet()
			#设置子弹精灵的位置
			bullet1.rect.left = (self.rect.x+120)+i*20
			bullet1.rect.centery = self.rect.centery

			bullet2.rect.left = (self.rect.x+70)+i*20
			bullet2.rect.centery = self.rect.centery+32

			bullet3.rect.left = (self.rect.x+70)+i*20
			bullet3.rect.centery = self.rect.centery-32
			#将子弹精灵添加到精灵组
			self.bullets_group.add(bullet1,bullet2,bullet3)

#英雄精灵
class Hero_Two(GameSprite):

	def __init__(self):
		super().__init__("/home/lzb/images/life.png")
		self.rect.centery = SCREEN_RECT.centery-100
		self.rect.left = SCREEN_RECT.y
		self.Move = True
		#子弹精灵组
		self.bullet_group = pygame.sprite.Group()
	def update(self):
		#super().update()
		if not self.Move:
			self.rect.x += self.speed
		else:
			self.rect.y += self.speed

		#self.rect.y += self.speed
		#飞机飞出屏幕
		if self.rect.bottom <= 0:
		 	self.rect.y = self.rect.bottom+SCREEN_RECT.height
		elif self.rect.y >= SCREEN_RECT.height:
		 	self.rect.y = -self.rect.height

		if self.rect.x <= 0:
			self.rect.x = 0
		elif self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width
	def fire(self):
		for i in (1,2,3):
			#创建子弹精灵
			bullet2 = Bullet()
			bullet3 = Bullet()
			#设置子弹精灵的位置

			bullet2.rect.left = (self.rect.x)+i*20
			bullet2.rect.centery = self.rect.centery+20

			bullet3.rect.left = (self.rect.x)+i*20
			bullet3.rect.centery = self.rect.centery-20
			#将子弹精灵添加到精灵组
			self.bullet_group.add(bullet2,bullet3)



#子弹精灵
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("/home/lzb/images/bullet2.png")

	def update(self):
		# panduan = random.randint(0, 1)
		# if panduan == 0:
		# 	self.rect.y -= 5
		# 	self.rect.x += 5
		# else:
		# 	self.rect.y += 5
		# 	self.rect.x += 5
		self.rect.x += 20
		if self.rect.left >= SCREEN_RECT.width :

			self.kill()