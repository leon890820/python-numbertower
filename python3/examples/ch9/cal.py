def main() :

    wstrs = ( "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" )
    w = 4 
    fmt = "{:>" + str(w) + "}" 

    while True :

        y = int( input("輸入西元年> ") ) 

		# 由 1 月到 12 月
        for m in range(1,13) :

			# 列印月名與一周的星期字串
            print( " "*12 , m , "月" )
            for s in wstrs : print( fmt.format(s) , end="" ) 
            print() 
        
			# 計算每月一日是星期幾與當月的天數
            wday , mdays = weekday(y,m,1) , mondays(y,m) 

			# 先印每月一日之前的空格
            print( " "*int(w*wday) , end="" ) 

			# 列印每一天日期
            for d in range(mdays) :

                print( fmt.format(d+1) , end= ("" if wday<6 else "\n" ) )
                wday = ( wday + 1 if wday < 6 else 0 )  
            
            print("\n")

# 某年是否為閏年
def isleap( y ) :
    return True if y%400 == 0 or ( y%100 and y%4 == 0 ) else False 

# 某年某月的日數
def mondays( y , m ) :
    days = [ 31 , 28 , 31 , 30 , 31 , 30 , 
             31 , 31 , 30 , 31 , 30 , 31 ]
    if m == 2 :
        return 29 if isleap(y) else 28 
    else :
        return days[m-1] 
        
# 計算某年月日星期幾
def weekday( y , m , d ) :
    ( y , m ) = ( y-1 , m+10 ) if m < 3 else ( y , m - 2 )
    return ( y + y//4 - y//100 + y//400 + int(2.6*m-0.2) + d )%7 


# 執行主函式
main() 
