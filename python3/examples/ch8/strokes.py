
# 索引：萬國碼編號    對映值：筆劃數
sdict = {}

# 讀入筆劃檔存入 sdict 字典
with open( "strokes.dat" ) as infile :

    for line in infile :
        ucode , strokes = line.split()
        num = int(ucode[2:],16)
        sdict[num] = int(strokes)

# 輸入中文句子
while True :

    words = input("> ") 

    totals = 0
    for c in words :
        strokes = sdict[ord(c)]
        print( c , ":" , strokes , sep="" , end="  " ) 
        totals += strokes

    print( " 總筆劃數:" , totals , sep="" , end="\n\n" )
