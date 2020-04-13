class Bucket :

	# 初始方法：設定水桶容積與水容積
	def __init__( self , h , w = 0 ) :
		self.bucket_height , self.water_height = h , w

    # 字串表示方法
	def __str__( self ) :
		return ( "水桶高：" + str(self.bucket_height) + " ， " +
				 "水位高：" + str(self.water_height) )

	# 裝滿水	
	def fill_water( self ) :
		self.water_height = self.bucket_height 

	# 水倒光
	def empty_bucket( self ) :
		self.water_height = 0

	# 將水倒向 foo，水不得外溢
	def pour_to( self , foo ) :

		remain = foo.bucket_height - foo.water_height

		if self.water_height >= remain :
			foo.water_height = foo.bucket_height
			self.water_height -= remain
		else :
			foo.water_height += self.water_height
			self.water_height = 0

		return self				


	# 使用 A >> B 模擬 A 水桶倒向 B 水桶動作
	def __rshift__( self , foo ) :
		return self.pour_to(foo)

		
if __name__ == '__main__' :

	a , b = Bucket(5,0) , Bucket(3,0) 

	print( "> a , b 兩水桶容量分別為 5 公升與 3 公升 ：" )
	print( "  a：" + str(a) , "	 b：" + str(b) )
	print() 

	# a 先裝滿水後倒向 b
	a.fill_water()
	a >> b 
	print( "> a 先裝滿水後倒向 b ：" )
	print( "  a：" + str(a) , "	 b：" + str(b) )
	print() 

	# b 倒光後，a 再倒水到 b
	b.empty_bucket()
	a >> b
	print( "> b 倒光後，a 再倒水到 b ：" )
	print( "  a：" + str(a) , "	 b：" + str(b) )
	print() 

	# a 先裝滿水後倒向 b
	a.fill_water()
	a >> b 
	print( "> a 先裝滿水後倒向 b ：" )
	print( "  a：" + str(a) , "	 b：" + str(b) )
