Day , Section = 5 , 8

cnum = '一二三四五'

# 中文數字對數字字串下標
c2n = { b : a for a , b in enumerate(cnum) }

# 兩維串列：儲存五天八節的課程名稱
wkclass = [ [None]*Day for i in range(Section) ]

with open("schedule.dat") as infile :

    for line in infile :

        course , *csect = line.split()
        
		# p 為 星期幾:節數，例如：四:567
        for p in csect :

            a , b = p.split(':')

			# w 為 wkclass 的第二個下標
            w = c2n[a]             

            for c in b :
				# s 為 wkclass 的第一個下標
                s = int(c)-1       
                wkclass[s][w] = course[0]

# 印出課程表
print( "   | " + " ".join( cnum ) )
print( "-"*(5+3*5) )

for s in range(Section) :

    if s == 4 : print( "-"*(5+3*5) )
    print( " "+str(s+1)+" | " , end="" )

    for w in range(Day) :
        print( wkclass[s][w] if wkclass[s][w] else "  " , end=" " )

    print()
