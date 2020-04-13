while  True :
 
	n = int( input("> ") ) 

	# 山
	for i in range(n) :

		for j in range(-n+1,n) :

			s = abs(j)                 # 山高至頂端距離
			h = n - s                  # 山高
			w = 2 * ( n - abs(j) )     # 山寬
			t = i - s                  # 山頂往下距離

			if i < s : 
				print( " "*w , end="" )
			else :
				print( " "*(n-1-i)+"/"+"*"*(2*t)+"\\"+" "*(n-1-i) , end="" )

		print()
			
	# 水
	for i in range(2) :

		for j in range(-n+1,n) :

			w = 2*(n-abs(j))
			print( "~"*w , end="" )

		print()

	print()
