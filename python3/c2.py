import pylab
a=-5
b=5
n=1000
for n in range(1000,10000,1000):
    xs=pylab.linspace(a,b,n,endpoint=False)
    ys=((b-a)/n)*(xs**2-1)
    sum1=sum(ys)
    print(sum1)
for i in range(1,5):
    xs=pylab.linspace(-i,i,n,endpoint=False)
    ys=((2*i)/n)*((pylab.exp(-(xs**2)/2))/(pylab.sqrt(2*pylab.pi)))
    sum1=sum(ys)
    print(sum1)
    
