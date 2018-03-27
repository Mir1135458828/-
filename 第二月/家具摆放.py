#家具类
class HOuseItem(object):

	#初始化家具
	def __init__(self,name,area):
		
		self.name = name
		self.area = area

	
	#输出家具信息
	def __str__(self):

		return "家具名称：%s 		占地面积：%.2f平米"%(self.name,self.area)



#房子类
class House(object):
	item_list = []
	#初始化房子信息
	def __init__(self,house_type,area):
		self.house_type = house_type
		self.area = area
		#默认剩余面积和初始面积相同
		self.free_area = self.area
		#新房子没有家具
		
	#添加家具
	def add_item(self,jiaju,mianji):
		if self.free_area >=mianji:
			print("添加了:%s"%jiaju)
			House.item_list.append(jiaju)
			self.free_area -= mianji

	#输出房子信息
	def __str__(self):
		return "户型:%s    \n占地面积：%d    \n剩余面积:%.2f平米    \n家具:%s"%(self.house_type,self.area,self.free_area,House.item_list)



#创建家具的对象
bed = HOuseItem("床 ", 4)
print(HOuseItem(bed.name,bed.area))
chest = HOuseItem("衣柜", 2)
print(HOuseItem(chest.name,chest.area))
table = HOuseItem("餐桌", 1.5)
print(HOuseItem(table.name,table.area))

#创建房子对象
bothy = House("茅屋", 20)

#添加家具并且输出房子信息
bothy.add_item(bed.name,bed.area)
bothy.add_item(chest.name,chest.area)
bothy.add_item(table.name,table.area)
print(House(bothy.house_type,bothy.free_area))







