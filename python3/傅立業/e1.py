import pylab
t=pylab.linspace(0,2*pylab.pi,10000)
xs=0*t
for i in range(1000):

    xs+=4*pylab.sin(t*(2*i+1))/(pylab.pi*(2*i+1))
pylab.plot(t,xs)
pylab.show()
