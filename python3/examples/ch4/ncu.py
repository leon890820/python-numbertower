# 「中大」兩字的點矩陣
ncu = ( (0x4,0x1f,0x15,0x1f,0x4) , (0x4,0x1f,0x4,0xa,0x11) ) 

R , C = len(ncu[0]) , 5 

# 大縱向
for s in range(R) :

	# 小縱向
    for r in range(R) :

        print( " " , end="" )

		# 每個中文字
        for k in range(len(ncu)) :

			# 大橫向
            for t in range(C-1,-1,-1) :

				# 小橫向
                for c in range(C-1,-1,-1) :

					# 檢查列印條件是否滿足
                    if ( ( ncu[k][r] & ( 1 << c ) ) and 
						 ( ncu[k][s] & ( 1 << t ) ) ) :
                        print( "o" , end="" )
                    else :
                        print( " " , end="" )

                print( " " , end="" )

            print( "   " , end="" )

        print() 
