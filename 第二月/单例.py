class Dog(object):
	count = 0
	ins = None
	Bool = False
	def __new__(cls,*a,**b):
		if cls.ins is None:
			cls.ins = super().__new__(cls)
		return cls.ins

	def __init__(self,name,six):
		
		if not Dog.Bool:
			Dog.count+=1
			self.name = name
			self.six = six
			Dog.Bool = True
			print(Dog.count)
q = Dog("小明", "男")
print(q.count)
print(q.name)
print(q.six)
w = Dog("小红", "女")
print(w.count)
print(w.name)
print(w.six)

print(id(q))
print(id(w))