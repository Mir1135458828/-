#人类作为一个基类
class Person(object):

	#会玩游戏
	def play_computergames(self):
		print("玩游戏")
	#会睡觉
	def sleep(self):
		print("睡觉")


#继承Person类
class Father(Person):

	#初始化
	def __init__(self,name):
		self.name = name
	#重写父类的方法
	def play_computergames(self):
		print("%s在玩游戏"%self.name)


#继承Person类
class Mather(Person):

	#初始化
	def __init__(self,name):
		self.name = name
	#重写父类方法
	def sleep(self):
		print("%s累了，要睡觉"%self.name)


#单例模式	  独生子
class Son(object):

	#用来判断并控制只有一个地址
	instance = None
	#用来判断并控制只有一个实例化对象
	is_instance = False

	#确定返回的只有一个地址
	def __new__(cls,*q,**w):
		if Son.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance

	#永远只有一个实例对象
	def __init__(self,name):
		
		if not Son.is_instance:
			print("我是爸爸妈妈唯一的孩子")
			self.name = name
			Son.is_instance = True

	#将 Fatner 和 Mather 的实例对象作为参数放进去  实现多态
	def play_with_family(self,Father,Mather):
		print("%s和%s%s出去旅游了"%(self.name,Father.name,Mather.name))

#Father实例对象
baba = Father("爸爸")
baba.play_computergames()

#Mather实例对象
mama = Mather("妈妈")
mama.sleep()

#Son实例对象  单例模式只有一个地址和实例对象
xiaoming = Son("小明")
xiaoming.play_with_family(baba,mama)

#再创建一个作为比较
xiaohong = Son("小红")

print("地址".center(20, "-"))
print(id(xiaoming))
print(id(xiaohong))

print("名字".center(20, "-"))
print(xiaoming.name)
print(xiaohong.name)

