def main() :

	global	c2n 

	cnum = '一二三四五'
	c2n = dict( [ ( b , a ) for a , b in enumerate(cnum) ] )

	# 讀檔
	with open("schedule.dat") as infile :
		schedules = infile.readlines()

	# 依據課程在一周內最早上課時間排序
	schedules.sort( key=by_weekly_earlier_hr )

	# 列印
	for s in schedules : 
		print( s.strip() )

# 設定排序標準
def	 by_weekly_earlier_hr( schedule ) :

	global c2n 

	# 分解課名與上課時間
	course , *csect = schedule.split()
	
	all = []
	for p in csect :
		# 拆解上課時間
		a , b = p.split(':')
		w = c2n[a] 

		# 將此門課所有上課時間以整數表示
		for c in b :
			s = int(c) 
			all.append(w*10+s) 
			
	# 回傳該門課在一周最早上課時間所代表的整數
	return	min(all)

# 執行主函式	
main()
