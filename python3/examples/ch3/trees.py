while True :

	n = int( input("> ") )
	a = 3 * n + 2 

	for i in range(a) :

		for j in range(-n+1,n) :

			s = abs(j)                # 樹與中間樹單位距離
			f = n - s                 # 樹幹高
			h = 2 * n + 1 - 2 * s     # 樹身高
			w = 4 * ( n - s ) + 1     # 樹身底寬
			d = 3 * s                 # 樹梢與頂部距離	  

			if i < d : 
				print( " "*w , end=" " ) 

			elif i < d+h :
				print( " "*(d+h-i-1)+"*"*(2*(i-d)+1)+" "*(d+h-i-1) , end=" " )

			elif i < d+h+f :
				print( " "*(2*(n-s))+"|"+" "*(2*(n-s)) , end=" " ) 

			else :
				print( "="*(2*(n-s))+"="+"="*(2*(n-s)) , 
					   end=("=" if j<n-1 else " ") ) 

		print() 

	print()
