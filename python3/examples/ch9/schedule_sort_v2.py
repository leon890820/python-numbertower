def main() :

	global	snum

	cnum = '一二三四五'
	c2n = dict( [ ( b , a ) for a , b in enumerate(cnum) ] )

	# 課程與上課時間
	schedules = []

	# 字典，儲存課名與一周最早上課時間比較數字
	snum = {}

	# 讀檔
	with open("schedule.dat") as infile :

		for line in infile :

			schedule = line.strip()
			schedules += [ schedule ]

			# 回傳課程與其一周最早上課時間比較數字
			course , num = course_eariler_number(schedule,c2n)

			# 存入字典
			snum[course] = num

	# 依據課程在一周內最早上課時間排序
	schedules.sort( key = lambda s : snum[s.split()[0]] )

	# 列印
	for s in schedules : 
		print( s.strip() )


# 尋找最早上課時間代表數字
def  course_eariler_number( schedule , c2n ) :

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
	
	return ( course , min(all) )


# 執行主函式    
main()
