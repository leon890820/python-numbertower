nations , gdps , years = [] , [] , []

with open("edu.dat") as infile :

    for line in infile :

        if line.isspace() : continue

        # 星號將多字串的國家名稱儲存到串列
        *nation , gdp , year , src = line.split() 

        # 儲存國名與年度資料於串列
        nations.append( " ".join(nation) )
        years.append( year ) 

        # 沒有資料時，gdp 以 -1 替代
        if year == "n.a." :
            gdps.append( -1 )
        else :
            gdps.append( float(gdp) )

i = 1

# 依 gdp 由大到小，國名依字母順序排列
for nation , gdp , yr in sorted( zip(nations,gdps,years) , 
                                 key=lambda p : ( -p[1] , p[0] ) ) :

    if gdp == -1 : 
        line = "{:>3}:{:>5} [{:>4}] {:}".format( i , "---" , 
                                                 yr , nation ) 
    else :
        line = "{:>3}:{:>5.1F} [{:>4}] {:}".format( i , gdp , 
                                                    yr , nation ) 

    print( line )
    i += 1
