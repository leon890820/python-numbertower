import math

# 使用 lambda 設定函數
# 函數 : x**2 - 2   與一次微分： 2x 
f  = lambda x : x**2 - 2
df = lambda x : 2*x

# 根
r = math.sqrt(2)

# 二分逼近法
a , b , k = 1 , 2 , 0
fa , fb = f(a) , f(b)
tol1 = 1.e-5

print( "> 二分逼近法： 起始區間 (", a , "," , b , ")" , sep=""  ) 

while True :

	c = (a + b)/2
	err = abs(c-r)
	k += 1

	# 迭代次數 近似根 誤差，以下 10e 代表以 10 格與科學記號呈現數字 
	print( "{:<2} : {:<10e} {:<10e}".format(k,c,err) , sep="" )

	fc = f(c)

	# 函數絕對值小於 tol1 才跳離迭代
	if abs(fc) < tol1 : break 

	if fc * fa < 0 :
		b = c
		fb = fc
	else :
		a = c
		fa = fc

print()

# 牛頓迭代法
a , k , tol2 = 2 , 0 , 1.e-14
err = abs(a-r)

print( "> 牛頓迭代法：" ) 
print( "{:<2} : {:<10e} {:<10e}".format(k,a,err) , sep="" )

while True :
	
	b = a - f(a)/df(a)
	err = abs(b-r)
	k += 1

	# 迭代次數 近似根 誤差，以下 10e 代表以 10 格與科學記號呈現數字 
	print( "{:<2} : {:<10e} {:<10e}".format(k,b,err) , sep="" )

	# 函數絕對值小於 tol2 才跳離迭代
	if abs(f(b)) < tol2 : break 

	a = b 
