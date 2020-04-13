for i in range(2,10000):
    m=i
    k=2
    print(i,'=',end=' ')
    while m>1:
        if m%k==0:
            print(k,end=' ')
            m=m//k
            if m==1:
                print(' ')
            else:
                print('x',end=' ')
        else:
            k+=1
        
