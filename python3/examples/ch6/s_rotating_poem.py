poem = ( "寒泉漱玉清音好" "好處深居近翠巒" 
         "巒秀聳岩飛澗水" "水邊松竹檜宜寒"
         "寒窗淨室親邀客" "客待閒吟恣取歡" 
         "歡宴聚陪終席喜" "喜來歸興酒闌殘" ) 

# n     列(行)數
# r , c 位置下標
# d     方向  
n , r , c , d  = 7 , 5 , 1 , 0

# 轉彎方向
dr , dc = [ 0 , -1 , 0 , 1 ] , [ -1 , 0 , 1 , 0 ]

# 二維字串串列
p = [ [ "  " ] * n for i in range(n) ]

for i , ch in enumerate(poem) :

	# 跳過重複字不處理
	if i > 0 and i%n == 0 : continue

	# 設定 p 
	p[r][c] = ch
	
	# 更新 r 與 c 位置
	r += dr[d] 
	c += dc[d] 

	# 檢查是否該轉彎
	if ( ( r == c ) or ( r == 5 and c == 0 ) or 
		 ( r < c and r+c == n-1 ) or ( r > c and r+c == n ) ) :
		d += 1
		if d == 4 : d = 0

# 列印
for i in range(n) :	 
	print( " ".join(p[i]) )

