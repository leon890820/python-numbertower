import pylab

#------------------------------------------
# y' = x**(1/3) sin(x) + 0.2
#
# i.c.  y(0) = val     val = range(0,11,5)
#------------------------------------------
def fn(x) :
    return  x**(1/3) * pylab.sin(x) + 0.2

# 設定周邊空白區域為白色
pylab.figure(facecolor='white')

# 設定 [a,b] 與執行次數
a , b , n = 0 , 20*pylab.pi , 500 
dx = (b-a)/n

# 設定 xs , ys 
xs = [ a + i*dx for i in range(n+1) ]
ys = [None] * (n+1) 

# c ：起始值，在此分別為 0 5 10 三數
# 以下計算相同微分方程式但不同起始值的解答
for c in range(0,11,5) :

    ys[0] = c

    for i in range(n) :
        ys[i+1] = ys[i] + dx * fn(xs[i])  
        
    sym = 'y(0) = ' + str(ys[0])

    pylab.plot(xs,ys,label=sym,lw=2)

# 設定圖形標頭文字
pylab.title(r"$y' = \sqrt[3]{x}\, \sin(x) + 0.2$",fontsize=20)

# 設定 X 軸與 Y 軸文字
pylab.xlabel('X')
pylab.ylabel('Y')

# 設定各線條圖例位置
pylab.legend(loc='upper left')

pylab.show()
