def main() :

	global sdict 

	# 1：讀入筆畫檔，設定 sdict 字典(由 字-->筆劃)
	sdict = {}
	read_strokes( sdict ) 

	# 2：讀入成語檔，設定 idioms 成語串列
	idioms = []
	read_idioms( idioms ) 

	# 3：依各字筆劃數排序
	idioms.sort( key = by_strokes ) 

	# 4：列印排序後的成語
	print_idioms( idioms , sdict ) 


# 讀取筆劃檔，設定 sdict 字典(由 字-->筆劃)
def read_strokes( sdict ) :

	with open( "strokes.dat" ) as infile :

		for line in infile :
			ucode , strokes = line.split()
			ch = chr(int(ucode[2:],16))
			sdict[ch] = int(strokes)

	
# 讀入成語檔，設定 idioms 成語串列
def read_idioms( idioms ) :

	with open("idioms.dat") as infile :

		for line in infile : 
			idioms += [ line.strip() ]
 

# 排序標準：依各字筆劃數排序
def by_strokes( idiom ) :

	global	sdict 
	return [ sdict[c] for c in idiom ] 


# 列印成語
def print_idioms( idioms , sdict ) :

	s1 = 0
	for ws in idioms :
		s2 = sdict[ws[0]]
		if s1 != s2 : 
			if s1 : print()
			print( s2 , "畫：" )

		print( ws , "-".join( map( lambda c : str(sdict[c]) , ws ) ) ) 
		s1 = s2


# 執行主函式
main()	
