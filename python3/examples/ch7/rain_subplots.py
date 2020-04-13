import pylab 

n = 4
all_sumlocs = [] 
totals = []

with open( "rain.dat" ) as infile :

	# 跳過中文測站名稱
	infile.readline()

	# 讀取百分比加權數
	wname , *weights = infile.readline().strip().split()

	for k , line in enumerate(infile) :

		date , hr , *srainfall  = line.strip().split()
		
		rainfall = [ int(x) for x in srainfall ] 

		if k%n == 0 :
			# 第一個小時
			sumloc = rainfall
		else :
			# 第二個小時後雨量加總
			sumloc = list( map( lambda x , y : x+y , sumloc , rainfall ) ) 

		if (k+1)%n == 0 :
			all_sumlocs += [ sumloc ]

			# 計算集水區每 4 個小時的平均雨量
			totals += [ sum( map( lambda x , y : x*float(y)/100 , 
								  sumloc , weights ) ) ]

# 找出所有測站的最大雨量
maxr = 0
for x in all_sumlocs : 	maxr = max( *x , maxr )

# 調整為雨量最大刻度值
maxr = int(pylab.ceil(maxr/50)*50)

# 子圖橫縱向數量
nrows , ncols = 2 , 3 

# 區分 2x3 圖形六圖，共用 x , y 軸
fig , gs = pylab.subplots(nrows,ncols,sharex='all',sharey='all',
						  facecolor='w')

# hspace 設定縱向兩圖間的間距(平均縱軸高度的比例)
# wspace 設定橫向兩圖間的間距(平均橫軸寬度的比例)
pylab.subplots_adjust(hspace=0.4,wspace=0.2)

# X 座標
xs = [ x+1 for x in range(len(weights)) ]

# 直條圖的 rgb 色碼
cs = ( 0.1 , 0.6 , 0.8 )

# k 圖形順序下標
k = 0

# 給 xs 與 sumloc 畫直條圖
for i in range(nrows) :

	for j in range(ncols) :

		# 畫直條圖
		gs[i][j].bar(xs,all_sumlocs[k],align='center',color=cs)

		# 設定各直條圖的刻度文字：以大寫字母代替
		pylab.setp( gs[i][j] , xticks = xs ,
					xticklabels = [ chr(ord('A')+i) 
									for i in range(len(weights))] )

		# 顯示區域，格線
		gs[i][j].axis( (0,11,0,maxr) )
		gs[i][j].grid()

		# 設定 x 軸與 y 軸文字
		gs[i][j].set_xlabel('Location')
		gs[i][j].set_ylabel('Rainfall in mm')

		# 設定圖形標頭文字
		gs[i][j].set_title( date + ' [{:0>2}-{:0>2}]'.format(k*4,(k+1)*4) + 
							' : ' + "{:6.2f}".format(totals[k]) + ' mm' , 
							color='r' , fontsize=14 )
		k += 1

pylab.show()
