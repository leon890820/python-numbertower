n=int(input())
import random
c=[x for x in range(-n+1,n)]
random.shuffle(c)
for i in range(3*n+2,-2,-1):
    for j in c:
        s=abs(j)
        f=n-s+1
        m=3*s
        h=3*n+2-f-m
        w=2*h-1
        if i>h+f:
            print(' '*w,end=' ')
        elif i==f+h:
            print(' '*(i-f-1)+'*'+' '*(i-f-1),end=' ')
        elif f<i<f+h:
            print(' '*(i-f-1)+'/'+'-'*((h+f-i)*2-1)+'\\'+' '*(i-f-1),end=' ')
        elif i==f and f>2:
            print('|'+' '*(n-s+1)+'_'*((n-s-1)*2-1)+' '*(n-s+1)+'|',end=' ')
        elif i==f and f==2:
            print('|'+' '*(3+(n-s-1)*4)+'|',end=' ')
        elif 1<i<f :
            print('|'+' '*(n-s)+'|'+' '*((n-s-1)*2-1)+'|'+' '*(n-s)+'|',end=' ')
        elif i==1:
            print('|'+'='*(3+(n-s-1)*4)+'|',end=' ')
        else:
            print('II'+' '*(1+(n-s-1)*4)+"II",end=' ')
    print()    
