# 0 到 9 數字點矩陣
bmap = ( (15,9,9,9,15),  (2,2,2,2,2),    (15,1,15,8,15), (15,1,15,1,15),
         (9,9,15,1,1),   (15,8,15,1,15), (15,8,15,9,15), (15,1,2,2,2),
         (15,9,15,9,15), (15,9,15,1,15) )

# 每個點矩陣的橫列數與直行數
R , C = len(bmap[0]) , 4 

while True :

	num = input("> " )	

	# nos 為 num 的各個位數串列
	nos = [ int(s) for s in list(num) ]		# num 也可不用置於 list() 內

	print()

	# 數字的每一列
	for r in range(R) :

		# 每個數字
		for n in nos :

			# 數字的每一行
			for c in range(C-1,-1,-1) :

				# 判斷位元位置是否有值
				if bmap[n][r] & ( 1 << c ) :
					print( n , end="" )
				else :
					print( " " , end="" )

			print( "  " , end="" )

		print()

	print()
