# 索引：筆劃   對映值：同筆劃漢字所構成字串
sdict = {}

# 讀筆劃資料檔，將同筆劃的字存在一起
with open( "strokes.dat" ) as infile :

    for line in infile :
        ucode , strokes = line.split()

        char = chr(int(ucode[2:],16))
        stroke = int(strokes)

        # 若筆劃數第一次出現，以字串儲存
        if stroke not in sdict :
            sdict[stroke] = char 
        else :
            sdict[stroke] += char 

# 依筆劃由小到大排序
for  stroke in sorted( sdict.keys() ) :

    chars = sdict[stroke]  
    print( stroke , "劃 :" , len(chars) , "個" )

    a = 0
    while a < len(chars) :
        print( " ".join(chars[a:a+20]) ) 
        a += 20
        
    print()
        
