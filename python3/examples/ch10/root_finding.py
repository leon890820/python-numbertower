from math import *
import pylab

# 函式
def fn( x ) :
	return	x * cos(x) - 5 * sin(x/10) + 4

# 計算微分
def df( x , h=1.e-7 ) :
	return	( fn(x+h) - fn(x-h) ) / (2*h)

# 在 [a,b] 間畫圖，npts 為點數 
def plot_fn( a , b ,  npts = 100 ) :

	dx = ( b - a ) / (npts-1)
	xs = [ a + i * dx for i in range(npts) ]
	ys = [ fn(x) for x in xs ]

	pylab.figure(facecolor='white')
	pylab.grid()
	pylab.xlabel("x")
	pylab.ylabel("f(x)")
	pylab.plot( xs , ys )  
	pylab.show() 


# 定義求根基礎類別
class Root_Finding : 

	def __init__( self , err = 1.e-10 ) :
		self.n , self.err = 0 , err

	# 設定收斂誤差
	def set_err( self , err ) : self.err = err

	# 迭代次數
	def iter_no( self ) : return self.n 


# 二分逼近法
class Bisection(Root_Finding) :

	def __init__( self , err = 1.e-10 ) :
		super().__init__(err) 

	def __str__( self ) : return "Bisection method" 

	# 二分求根法：在 [a,b] 區間內求根
	def find_root( self , a , b ) :

		fa , fb , n = fn(a) , fn(b) , 1

		while True :
			c = ( a + b ) / 2
			fc = fn(c) 

			if abs(fc) < self.err : break 

			if fa * fc < 0 :
				b , fb = c , fc
			elif fb * fc < 0 :
				a , fa = c , fc

			n += 1

		self.n = n
		return c 


# 割線法
class Secant(Root_Finding) :

	def __init__( self , err = 1.e-10 ) :
		super().__init__(err) 

	def __str__( self ) : return "Secant method" 

	# 割線求根法：由 a , b 兩點起始
	def find_root( self , a , b ) :

		fa , fb , n = fn(a) , fn(b) , 1

		while True :
			c = b - fb * (b-a) / (fb-fa) 
			fc = fn(c)
			if abs(fc) < self.err : break 

			a , b = b , c 
			fa , fb = fb , fc
			n += 1

		self.n = n 
		return c

	
# 牛頓迭代法
class Newton(Root_Finding) :

	def __init__( self , err = 1.e-10 ) :
		super().__init__(err) 

	def __str__( self ) : return "Newton's method" 

	# 牛頓求根：由點 x1 起始
	def find_root( self , x1 ) :

		n = 1
		while True :
			x2 = x1 - fn(x1)/df(x1) 
			if abs(fn(x2)) < self.err : break 
			x1 , n = x2 , n+1
			
		self.n = n 
		return x2


if __name__ == '__main__' :

	# 畫函式圖形
	plot_fn(-10,10,200)
	
	foo = Bisection() 
	rt = foo.find_root(2,3) 
	print( "{:<17}:[{:>2}] {:>9.7f} {:>10.3e}".format( 
    	   str(foo) , foo.iter_no() , rt , fn(rt) ) )

	foo = Secant() 
	rt = foo.find_root(2,3) 
	print( "{:<17}:[{:>2}] {:>9.7f} {:>10.3e}".format( 
		   str(foo) , foo.iter_no() , rt , fn(rt) ) )

	foo = Newton() 
	rt = foo.find_root(2) 
	print( "{:<17}:[{:>2}] {:>9.7f} {:>10.3e}".format( 
		   str(foo) , foo.iter_no() , rt , fn(rt) ) )

