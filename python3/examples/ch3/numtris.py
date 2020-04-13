while  True :
 
	n = int( input("> ") ) 

	# 大縱向
	for s in range(n) :

		# 小縱向
		for i in range(n) :
		
			print( " "*((n-1-s)*n) , end="" )
		
			# 大橫向
			for t in range(s+1) :
	 
				print( " "*(n-1-i)+str(i+1)*(2*i+1)+" "*(n-1-i) , end=" " )
		
			print()

	print()
