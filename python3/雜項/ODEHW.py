import math 
def fun(x,y):
    return 2*y

x=0
y=1
h=0.05
print("x=",x+h,"y=",y)
while(x<0.15):
    k1=fun(x,y)
    k2=fun(x+0.5*h,y+0.5*h*k1)
    k3=fun(x+0.5*h,y+0.5*h*k2)
    k4=fun(x+h,y+h*k3)
    y=y+(h/6)*(k1+2*k2+2*k3+k4)
    if x==0:
        print(k1,k2,k3,k4)
    print("x=",x+h,"y=",y)
    x+=h

    

