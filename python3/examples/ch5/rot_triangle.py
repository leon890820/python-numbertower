import pylab

xs , ys = [ 0 , 1 , 0.5 ] , [ 0 , 0 , pylab.sqrt(3)/2 ]
colors = "rgbcmyk"

pylab.figure(facecolor='w')

pi = pylab.pi

# 六個旋轉三角形
for k in range(6) :

    cosk , sink = pylab.cos(k*pi/3) , pylab.sin(k*pi/3) 

	# 大三角形
    px , py = [ *xs[:] , xs[0] ] , [ *ys[:] , ys[0] ] 

	# 先旋轉大三角形到相關位置
    for i in range(len(px)) :
        px[i] , py[i]  = cosk*px[i] - sink*py[i] , sink*px[i] + cosk*py[i] 

    qx , qy = px[:] , py[:]

    r = 0.9 if k%2==0 else 0.1 

    # 再對每個大三角形內部旋轉 25 次
    for i in range(25) :

        pylab.plot(px,py,colors[k],lw=1.5)

        for j in range(3) :
            qx[j] =  r * px[j] + (1-r) * px[j+1] 
            qy[j] =  r * py[j] + (1-r) * py[j+1] 

        qx[-1] , qy[-1] = qx[0] , qy[0]

        px , py = qx[:] , qy[:]

pylab.axis('off')
pylab.show()

