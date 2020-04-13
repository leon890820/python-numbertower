import random 

while True :

	# 斜條線數量
	n = int( input("> ") )

	# m 最長直線高
	# w 直條圖寬 
	m , w = 9 , 3

	# 使用亂數設定各直條線長
	vals = [ random.randint(1,m) for i in range(1,n+1) ]

	# 畫直條線
	for s in range(m,0,-1) :
		
		for val in vals :

			if s > val :
				print( " "*w , end=" " )
			elif s == val :
				print( "\\" + str(val) + "/" , end=" " )
			else :
				print( " | " , end=" " )

		print() 

	# 畫底部等號
	print( "="*( (w+1)*n - 1) )
