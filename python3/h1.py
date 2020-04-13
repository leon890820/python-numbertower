m=[4,1,2,2,28]
c=0
r=0
c1=0
import random
for i in range(10000000):
    m=[4,1,2,2,28]
    c=0
    while c<9 :
        r=random.randint(0,4)
        if m[r]>0:
            m[r]-=1
            c+=1
    if m[4]==28:
        c1+=1
       
print(c1/100000,"%")        
        
    
        
