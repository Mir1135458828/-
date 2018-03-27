class Animal(object):
	def __init__(self,name):
		self.name = name
	def play(self):
		print(self.name,"在玩耍")

class Dog(Animal):
	def play(self):
		 print(self.name,"怼到天上去玩了")


class Person(object):
	def __init__(self,name):
		self.name = name
	def play_dog(self,dog):
		print(self.name+"和"+dog.name)
		
dog = Dog("哮天犬")
p = Person("小明")
p.play_dog(dog)