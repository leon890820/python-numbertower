import pylab

# 索引：洲名，對映值：( 國名 + 資料年份 , gdp ) 串列
ctn = {}

with open("edus.dat") as infile :

	for line in infile :

		# 分離資料再重新組合 ( 國名+年 , gdp ) 常串列
		*nation , gdp , year , continent = line.split() 
		if gdp == 'n.a.' : gdp = "-1"
		data = ( " ".join(nation) + " [" + year + "]" , float(gdp) ) 

		# 跨兩洲的國家以斜線分割：如俄羅斯
		for c in continent.split('/') :
			if c in ctn :
				ctn[c].append( data )
			else :
				ctn[c] = [ data ]

no = 5
xs = [ x for x in range(0,17,2) ]
ys = [ y for y in range(no,0,-1) ]

colors = 'rgbcmyk'

nrows , ncols = 3 , 2

# 區分 3x2 圖形五圖，共用 x , y 軸
fig , gs = pylab.subplots(nrows,ncols,facecolor='w')

# hspace 設定縱向兩圖間的間距(平均縱軸高度的比例)
# wspace 設定橫向兩圖間的間距(平均橫軸寬度的比例)
pylab.subplots_adjust(hspace=0.8,wspace=0.5)


# 依洲名排序
for i , k in enumerate( sorted( ctn.keys() ) ) :

	r = i//ncols
	c = i%ncols 

	# 各洲國家排列：先比 gdp 再比國名
	ctn[k].sort( key = lambda p : ( -p[1] , p[0] ) ) 

	# 儲存前 no 筆資料 vals：gdp% , nations：國名
	vals , nations = [] , []
	for j , p in enumerate(ctn[k]) :
		vals.append(p[1])
		nations.append(p[0]) 
		if j+1 == no : break  

	# 設定第一名國家顏色與其餘四國顏色不同
	gs[r][c].barh( ys[0],vals[0],align='center',color=colors[i] )
	gs[r][c].barh( ys[1:],vals[1:],align='center',color='#aaffaa' )

	# 設定子圖文字說明
	gs[r][c].set_title( "Top " + str(no) +
						" nations spend more gdp%\n on education in "
						+ k , color=colors[i] )

	# X 軸文字
	gs[r][c].set_xlabel("gdp percentage")

	# X 軸刻度
	gs[r][c].set_xticks(xs)

	# Y 軸刻度
	gs[r][c].set_yticks(ys)

	# Y 軸刻度文字
	gs[r][c].set_yticklabels(nations,color='k')

	# 顯示垂直格線
	gs[r][c].grid(axis='x')


# 去除最後一個圖形軸線
gs[2][1].axis('off')

pylab.show()
