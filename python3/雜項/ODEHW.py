import math 
x=1
y=1
h=0.05

xs=[]
ys=[]
c=1
while(x<1.5):
    y1=y+h*(x*y**2-y/x)
    x1=x+h
    y=y+(h*((x*y**2-y/x)+(x1*y1**2-y1/x1)))/2
    x+=h
    print(c,end=" : ")
    print("{:>2}".format(x),y)
    c+=1