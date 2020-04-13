n = int( input( "> " ) )

ofile = "rain" + str(n) + ".dat" 

with open("rain.dat") as infile , open(ofile,"w") as outfile :

	# 讀寫前二列
	outfile.write(infile.readline())
	outfile.write(infile.readline())

	# 第三列以後
	for i , line in enumerate(infile) :

		date , hr , *rain = line.split()

		# 將字串數字轉型為整數
		rain = [ int(x) for x in rain ]         
		
		if i%n == 0 :
			# 每 n 小時雨量的第一個小時
			rsum = rain 
		else :
			# 每 n 小時雨量的第二個小時之後
			for k , rf in enumerate(rain) : 
				rsum[k] += rf 

		# 在 n 小時的倍數時，列印累積雨量
		if (i+1)%n == 0 : 

			arf = ( date + ":" + hr + 
					"  ".join( map( lambda x : "{:>5}".format(x) , rsum ) ) )
		
			outfile.write( arf + "\n" )
