import math

# 顏色類別
class Color :
	"顏色類別儲存：顏色名稱與 R G B 數值"

	nrgb = 3 

    # 起始方法
	def __init__( self , cname , r , g , b ) :
		self.cname = cname
		self.rgb = [ int(x) for x in [ r , g , b ] ]

	# 字串表示方法：輸出以十六進位表示的顏色強度與名稱
	def __str__( self ) :
		return ( ("{:0>2x}"*Color.nrgb).format( *(self.rgb) ) 
				 + " " + self.cname )

    # 回傳顏色名稱與各組合顏色強度
	def name( self )  : return self.cname
	def red( self )   : return self.rgb[0]
	def green( self ) : return self.rgb[1]
	def blue( self )  : return self.rgb[2]

	# 兩顏色的距離
	def distance_from( self , color ) :
		dr , dg , db = [ self.rgb[i]-color.rgb[i] for i in range(Color.nrgb) ]
		ravg = ( self.red() + color.red() ) / 2

		return math.sqrt( 2*dr**2 + 4*dg**2 + 3*db**2 + 
						  ravg*(dr**2-db**2)/256 )


if __name__ == "__main__" :

	# 顏色字典：( 顏色名稱 --> Color 物件 )
	colors = {}

	# 讀入顏色檔，將每個顏色存成 Color 物件存入 colors 字典
	with open("rgb.dat") as infile :
		for line in infile :
			cname , *rgb = line.split()
			colors[cname] = Color(cname,*rgb) 

	while True :

		color_name = input("> ")

		if color_name in colors :

			# 取得輸入顏色的顏色物件
			color = colors[color_name]

			print( "-->" + " "*6 , color )	

			# 計算輸入顏色與其他顏色的距離
			cpair = [ ( colors[x] , color.distance_from(colors[x]) ) 
					  for x in colors if x != color_name ] 

			# 利用排序找出顏色距離最小的前十筆相近顏色
			i = 1
			for c , d in sorted( cpair, 
								 key=lambda p : (p[1], p[0].name()) )[:10] :
				print("{:>2}: {:>5.1f} {:}".format(i,d,c))
				i += 1

		print()
