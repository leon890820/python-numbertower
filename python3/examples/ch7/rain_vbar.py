import pylab 

pylab.figure(facecolor='white')

with open( "rain.dat" ) as infile :

	# 跳過中文測站名稱
	infile.readline()

	# 讀取百分比加權數
	wname , *weights = infile.readline().strip().split()

	sumloc = [0] * len(weights)

	for line in infile :

		date , hr , *srainfall  = line.strip().split()

		rainfall = [ int(x) for x in srainfall ] 

		# 加總各個測站一天的雨量
		sumloc = list( map( lambda x , y : x+y , sumloc , rainfall ) ) 

# 計算集水區一天的平均雨量
total =  sum( map( lambda x , y : x*float(y)/100 , sumloc , weights ) ) 

xs = [ x+1 for x in range(len(weights)) ]

# 給 xs 與 sumloc 畫直條圖
pylab.bar(xs,sumloc,align='center',color='c')

# 設定各直條圖的刻度文字：以大寫字母代替
pylab.xticks(xs,[ chr(ord('A')+i) for i in range(len(weights))])

# 顯示區域，格線
pylab.axis( (0,11,0,500) )
pylab.grid()

# 設定 x 軸與 y 軸文字
pylab.xlabel('Location')
pylab.ylabel('Rainfall in mm')

# 設定圖形標頭文字
pylab.title('Average Rainfall : ' + "{:6.2f}".format(total) + 
            ' mm on ' + date, color='r',fontsize=16)

# 儲存圖形
pylab.savefig('rain_vbar.png')

pylab.show()
