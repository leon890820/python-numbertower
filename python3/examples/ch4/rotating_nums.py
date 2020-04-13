while True :

	n = int( input("> ") )

	# 二維串列儲存數字
	nums = [ [None]*n for i in range(n) ]

	# 起始位置
	s , t = 0 , 0 

	# 四個方向的前進方式
	ds , dt = [0,1,0,-1] , [1,0,-1,0]

	# m = n//2 的上取整函數值
	m = n//2 + ( 1 if n%2 else 0 ) 

	# 起始方向
	dir = 0
	for i in range(n*n) :

		nums[s][t] = i + 1

		# 判斷是否轉彎
		if s+t==n-1 or ( s >= m and s==t ) or ( s < m and s==t+1 ) :
			dir += 1 
			if dir == 4 : dir = 0

		# 更新位置
		s += ds[dir]
		t += dt[dir]

	# 列印數字
	print( "-"*(5*n+1) )
	for i in range(n) :
		for j in range(n) :
			print( "|{:>3}".format(nums[i][j]) , end=" " ) 
		print( "|" )
		print( "-"*(5*n+1) )

	print()
