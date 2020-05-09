import pylab
a,b=0,2*pylab.pi
n=10001
dx=(b-a)/(n-1)
xs=[a+dx*i for i in range(n)]
ys=[pylab.sin(x) for x in xs]
pylab.plot(xs,ys)
pylab.show()
