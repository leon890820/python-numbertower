import pylab
import random
ncu=[(0x8,0x8,0x7f,0x49,0x49,0x7f,0x8,0x8),(0x8,0x8,0x3e,0x2a,0x2a,0x7f,0x14,0x63)]
dt=pylab.linspace(0,12*pylab.pi,10000)
xs=pylab.sin(dt)*(pylab.exp(pylab.cos(dt))-2*pylab.cos(4*dt)+(pylab.sin(dt/12))**5)
ys=pylab.cos(dt)*(pylab.exp(pylab.cos(dt))-2*pylab.cos(4*dt)+(pylab.sin(dt/12))**5)

for i in range(8):
    for k in range(2):
        for j in range(6,-1,-1):
            if (ncu[k][i]>>j)%2==1:
                c=[random.random() for x in range(3)]
                theda=random.randint(0,360)*180/(pylab.pi)
                theda1=random.randint(0,360)*180/(pylab.pi)
                xs1=xs*pylab.cos(theda)-ys*pylab.sin(theda)
                ys1=xs*pylab.sin(theda)+ys*pylab.cos(theda)
                xs2=xs*pylab.cos(theda1)-ys*pylab.sin(theda1)
                ys2=xs*pylab.sin(theda1)+ys*pylab.cos(theda1)

                x1=random.randint(1,2)
                pylab.fill(xs1+(6-j+k*8)*10,ys1+(7-i)*10,color=c)
                for m in range(x1):
                    theda1=random.randint(0,360)*180/(pylab.pi)
                    pylab.fill((xs2*0.2+(6-j+k*8)*10)+pylab.cos(theda1)*8,ys2*0.2+(7-i)*10+pylab.sin(theda1)*8,color=c)

pylab.axis("off")
pylab.show()
