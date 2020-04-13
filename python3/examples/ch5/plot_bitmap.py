import pylab 

bmap = ( (15,9,9,9,15),  (2,2,2,2,2),    (15,1,15,8,15), (15,1,15,1,15),
         (9,9,15,1,1),   (15,8,15,1,15), (15,8,15,9,15), (15,9,1,1,1),
         (15,9,15,9,15), (15,9,15,1,15) )

# 每個點矩陣的橫列數與直行數
R , C = len(bmap[0]) , 4 

# 方框長度
s = 2

# 每一點所構成的方格座標
xs = pylab.array( [ 0 , s , s , 0 , 0 ] )
ys = pylab.array( [ 0 , 0 , s , s , 0 ] )

while True :

	# 輸入數字
	num = input("> ")

	pylab.figure(facecolor='w')

	# 每一列：由上到下
	for r in range(R) :

		# 每一個數字
		for k in range(len(num)) :

			n = int(num[k])    

			# 每一行：由右向左
			for c in range(C-1,-1,-1) :

				# 如果點存在
				if bmap[n][r] & ( 1 << c ) :

					# 將方格座標移到點的所在位置
					xs2 = xs + ( k*(C+1) + C-1-c ) * s
					ys2 = ys + ( R-1-r ) * s

					# 在 xs2 , ys2 方格以 red 填滿
					pylab.fill(xs2,ys2,color='r') 

	pylab.axis('off')
	pylab.show()
	
