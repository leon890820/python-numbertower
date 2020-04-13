import pylab

# 區分圖形為上下兩圖，共用 x 軸
f , gs = pylab.subplots(2, sharex=True,facecolor='w') 

# hspace 設定縱向兩圖間的間距(平均縱軸高度的比例)
# wspace 設定橫向兩圖間的間距(平均橫軸寬度的比例)
pylab.subplots_adjust(hspace=0.4,wspace=0)

n = int( input("> 傅立葉項數 : ") )

a , b , np = 0 , 2 , 401
xs , dx = pylab.linspace(a,b,np,retstep=True)

# ss：階梯函數    ys：傅立葉串列
ss = [ 1 if x<=1 else 0 for x in xs ]
ys = [ None ] * np

# 計算傅立葉 n 項的估算值
for i , x in enumerate(xs) :
    y , pix = 0 , pylab.pi * x
    for j in range(n) : y += pylab.sin((2*j+1)*pix)/(2*j+1)
    ys[i] = 0.5 + 2*y/pylab.pi

# 上圖
gs[0].plot(xs,ys,':r',label="Fourier series",lw=2)
gs[0].plot(xs,ss,'k',label="step function",lw=1)
gs[0].grid()
gs[0].set_xlabel("X")
gs[0].set_ylabel("Y")
gs[0].legend()
gs[0].set_title("Step function vs Fourier series with " + str(n) + " terms")

# 下圖
gs[1].fill_between(xs,ys,ss,color='r')
gs[1].grid()
gs[1].set_xlabel("X")
gs[1].set_ylabel("Y")
gs[1].set_title("Error of Fourier Series")

pylab.show()
