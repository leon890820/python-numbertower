def gcd( a , b ) :
    a , b = abs(a) , abs(b)
    if a > b :
        return gcd(a%b,b) if a%b else b
    else :
        return gcd(b%a,a) if b%a else a

class  Fraction :

    """分數類別：num : 分子  den : 分母"""

	# 起始方法
    def  __init__( self , n , d = 1 ) :
        self.num , self.den = n , d 

    # 使用字串設定分數
    @classmethod  
    def  fromstr( cls , fstr ) :
        if fstr.isdigit() :
            n , d = int(fstr) , 1
        else :
            n , d = map( int , fstr.split('/') )

        return  cls(n,d)

    # 使用帶分數設定分數
    @classmethod
    def  mixed_frac( cls , a = 0 , num = 0 , den = 1 ) :
        n , d = a * den + num , den
        return  cls(n,d)

    # 回傳最簡分數
    def simplest_frac( self ) :
        g = gcd(self.num,self.den) 
        return Fraction(self.num//g,self.den//g) 

    # 重新設定分數
    def set_val( self , n = 0 , d = 1 ) :
        self.num , self.den = n , d 

    # 取得分子與分母
    def get_num( self ) : return  self.num
    def get_den( self ) : return  self.den 

    # 分數加法
    def __add__( self , frac ) :
        n = self.num * frac.den + self.den * frac.num  
        d = self.den * frac.den 
        return Fraction(n,d).simplest_frac()

    # 分數減法
    def __sub__( self , frac ) :
        n = self.num * frac.den - self.den * frac.num
        d = self.den * frac.den 
        return Fraction(n,d).simplest_frac()

    # 分數乘法
    def __mul__( self , frac ) :
        n = self.num * frac.num
        d = self.den * frac.den 
        return Fraction(n,d).simplest_frac()

    # 分數除法
    def __truediv__( self , frac ) :
        n = self.num * frac.den 
        d = self.den * frac.num
        return Fraction(n,d).simplest_frac()

    # 分數 +=  
    def __iadd__( self , frac ) :
        self = self + frac
        return self

    # 分數 -=  
    def __isub__( self , frac ) :
        self = self - frac
        return self

    # 分數 *=  
    def __imul__( self , frac ) :
        self = self * frac
        return self

    # 分數 /=  
    def __itruediv__( self , frac ) :
        self = self / frac
        return self

    # < 
    def __lt__( self , frac ) :
        return True if self.num*frac.den < self.den*frac.num else False

    # == 
    def __eq__( self , frac ) :
        return True if self.num*frac.den == self.den*frac.num else False

    # >=  !=  <=  >
    def __ge__( self , frac ) : return  not ( self < frac ) 
    def __ne__( self , frac ) : return  not ( self == frac ) 
    def __le__( self , frac ) : return ( self < frac or self == frac ) 
    def __gt__( self , frac ) : return  not ( self <= frac ) 

    # 分數
    @classmethod
    def data_doc( cls ) : return  "num:分子 , den:分母"

    # 輸出分數字串表示分式
    def  __str__ ( self ) :
        if self.den == 1 :
            return str(self.num)  
        else :
            return "/".join( [ str(self.num) , str(self.den) ] ) 


if __name__ == "__main__" :

    f1 = Fraction(2,6) 
    f2 = Fraction.fromstr("2/4") 
    f3 = Fraction.mixed_frac(1,2,3) 

    print( Fraction.data_doc() )

    print( "f1 =" , f1 )  
    print( "f2 =" , f2 )  
    print( "f3 =" , f3 )  
    print()

    print( f1 , "+" , f2 , '=' , f1+f2 )
    print( f1 , "-" , f2 , '=' , f1-f2 )
    print( f1 , "*" , f2 , '=' , f1*f2 )
    print( f1 , "/" , f2 , '=' , f1/f2 )
    print()

    f3 += f1
    print( "f3 += f1  ---> f3 =" , f3 )  

    print()
    print( "f1 < f2" if f1 < f2 else "f1 >= f2" ) 
    print( "f1 == f2" if f1 == f2 else "f1 != f2" ) 
