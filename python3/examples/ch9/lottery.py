from random import *

def main() :

	# 樂透號碼數
	num = 6
	fset , cset = set() , set()

	# 產生 num 數字的中獎號碼
	lottery( fset , num ) 

	# 樂透中獎號碼
	wset = frozenset(fset)

	# 由小到大印出中獎號碼
	print( " ".join(map(lambda x : "{:>2}".format(str(x)),sorted(wset))) )

	# 彩券號碼
	for i in range(10) :

		fset = set()

		# 產生 num 數字彩券號碼
		lottery( fset , num )

		# 找出中獎號碼與彩券號碼相同數字
		cset = check_num(wset,fset)

		print( " ".join( map( lambda x : "{:>2}".format(str(x)),
							  sorted(fset))) ,
			   ':', len(cset) , '-->' , 
			   " ".join(map(str,sorted(cset))) ) 
		
# 產生 n 個號碼的樂透號碼
def lottery( bset , n ) :
	while True :
		bset.add( randint(1,49) ) 
		if len(bset) == n : return 

# 找出兩組樂透號碼的相同號碼
def check_num( aset , bset ) :
	return aset.intersection(bset)

# 執行主函式
main()
