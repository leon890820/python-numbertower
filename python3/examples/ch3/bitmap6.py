# 數字 6 的點矩陣縱橫方向為 5x4
r , c = 5 , 4 

while True :

	n = int( input("> ") ) 

	# 大縱向
	for s in range(r) :

		# 縱向重複次數
		for i in range(n) :

			# 大橫向
			for t in range(c) :

				# 橫向重複次數
				for j in range(n) :

					# 數字 6 的點陣滿足條件：
					if ( ( s%2==0 ) or t==0 or ( s==3 and t==3 ) ) :
						print( "6" , end="" )
					else :
						print( " " , end="" )

			# 換列
			print()
