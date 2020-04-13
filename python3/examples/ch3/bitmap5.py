# 點矩陣 5 為 rxc
r , c = 5 , 4 

while True :

	n = int( input("> ") ) 

	# 大縱向
	for s in range(r) :

		# 方塊縱向
		for i in range(n) :

			# 大橫向
			for t in range(c) :

				# 點矩陣 5 的方程式條件：
				if ( ( s==1 and t==0 ) or ( s==3 and t==3 ) or
					 ( s%2==0 ) ) :
					print( "5"*n , end="" )
				else :
					print( " "*n , end="" )

			# 換列
			print()
