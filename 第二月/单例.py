class Dog(object):
	
	ins = None
	Bool = False
	def __new__(cls,*a,**b):
		if cls.ins is None:
			cls.ins = super().__new__(cls)
		return cls.ins

	def __init__(self,name):
		
		if not Dog.Bool:
			self.name = name
			Dog.Bool = True

a = Dog("汪")
b = Dog("汪汪")

print(id(a))
print(id(b))

print(id(a.name))
print(id(b.name))
			
