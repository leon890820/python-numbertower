import math

cno = "零一二三四五六七八九十"

# 平面向量點
class Point :

    def __init__( self , x = 0 , y = 0 ) : self.x , self.y = x , y

    def __str__( self ) :
        return  "({:>3.1f},{:>3.1f})".format(self.x,self.y) 

    def get_x( self ) : return self.x 
    def get_y( self ) : return self.y 

	# pt1 + pt2
    def __add__( self , pt ) :
        return Point(self.x+pt.x,self.y+pt.y) 

	# pt1 - pt2
    def __sub__( self , pt ) :
        return Point(self.x-pt.x,self.y-pt.y) 

    # 點到原點長度
    def len( self ) : return math.sqrt(self.x**2+self.y**2) 

    # 旋轉點，輸入角度
    def rotate( self , ang ) :
        rang = ang*math.pi/180
        x = self.x * math.cos(rang) - self.y * math.sin(rang) 
        y = self.x * math.sin(rang) + self.y * math.cos(rang) 
        return Point(x,y)


# 多邊形基礎類別
class Polygon :

    def __init__( self , pts ) : self.pts , self.n = pts , len(pts) 
    def name( self ) : return cno[self.n] + "邊形" 

    def __str__( self ) : return self.name() + self.pts_str()

    # 座標點連接
    def pts_str( self ) :
        return "->".join( [ str(pt) for pt in self.pts ] )  

    # 旋轉座標點
    def rotate_pts( self , ang ) :
        return [ pt.rotate(ang) for pt in self.pts ]

    # 多邊形面積
    def area( self ) :
        a , n = 0 , self.n
        for i in range(n) :
            a += ( self.pts[i].get_x() * self.pts[(i+1)%n].get_y() -
                   self.pts[i].get_y() * self.pts[(i+1)%n].get_x() )
        return abs(a)/2 

    # 周長
    def perimeter( self ) :
        s = 0
        for i in range(self.n) :
            s += (self.pts[(i+1)%self.n]-self.pts[i]).len() 
        return s 

    # 旋轉
    def rotate( self , ang ) : return Polygon(self.rotate_pts(ang))
        

# 三角形繼承多邊形
class Triangle(Polygon) :

    # 三點座標
    def __init__( self , pts ) : super().__init__(pts)   
        
    @classmethod
    def from_pts( cls , pt1 , pt2 , pt3 ) : return  cls([pt1,pt2,pt3])

    def name( self ) : return "三角形" 

    def __str__( self ) :
        return ( self.name() + self.pts_str() + 
                 " 內接圓半徑：" + "{:<5.2f}".format(self.icircle_rad() ) )

    # 內接圓半徑
    def icircle_rad( self ) : return 2*super().area()/super().perimeter()

    # 旋轉
    def rotate( self , ang ) : return Triangle(super().rotate_pts(ang))
        

# 多邊形繼承多邊形
class Rectangle(Polygon) :

    # 三個相鄰點得矩形座標
    def __init__( self , pt1 , pt2 , pt4 ) :
        pt3 = pt2 + ( pt4 - pt1 ) 
        self.len1 , self.len2 = (pt2-pt1).len() , (pt4-pt1).len()
        super().__init__([pt1,pt2,pt3,pt4])  

    @classmethod
    def from_pt_len( cls , pt1 , len1 , len2 , ang=0 ) :
        pt2 = pt1 + Point(len1,0).rotate(ang) 
        pt4 = pt1 + Point(0,len2).rotate(ang) 
        return  cls(pt1,pt2,pt4)

    def name( self ) : return "長方形" 

    def __str__( self ) :
        return ( self.name() + self.pts_str() +
                 " 兩邊長：" + "{:} {:}".format(self.len1,self.len2) )

    def rotate( self , ang ) :
        pts = super().rotate_pts(ang)
        return Rectangle(pts[0],pts[1],pts[3])


# 正方形繼承長方形
class Square(Rectangle) :
    
    # 兩相鄰點得方形座標
    def __init__( self , pt1 , pt2 ) :
        pt4 = pt1 + (pt2-pt1).rotate(90)
        self.len = (pt2-pt1).len()
        super().__init__(pt1,pt2,pt4)   

    @classmethod
    def from_pt_len( cls , pt1 , len , ang=0 ) :
        pt2 = pt1 + Point(len,0).rotate(ang) 
        return  cls(pt1,pt2)

    def name( self ) : return "正方形"

    def __str__( self ) :
        return ( self.name() + super().pts_str() +
                 " 邊長：" + "{:}".format(self.len) )

    def rotate( self , ang ) :
        pts = super().rotate_pts(ang)
        return Square(pts[0],pts[1])


if __name__ == "__main__" :

    pt1 , pt2 , pt3 , pt4 = Point() , Point(2,0) , Point(2,3) , Point(0,1)

    gs = [ Polygon([pt1,pt2,pt3,pt4]) , 
           Triangle.from_pts(pt1,pt2,pt3) ,
           Rectangle.from_pt_len( pt1 , 2 , 3 , 90 ) , 
           Square.from_pt_len( pt3 , 5 ) ]

    for i , g in enumerate(gs) : 
        print(i+1,g," 面積："+str(g.area()))

    print("\n> 旋轉 90 度：") 
    for i , g in enumerate(gs) : print(i+1,g.rotate(90))
