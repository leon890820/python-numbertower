def countprime(n,v):
    if n==2: return 2
    n+=v 
    while True:
        findprime=False
        
        for i in range(2,n):
            if(n%i==0): 
                break
            i+=1
            if(i==n):
                findprime=True
                break
        if findprime:
            return n
        else: n+=v

n=int(input())

a=countprime(n,1)
b=countprime(a,1)
c=countprime(n,-1)
d=countprime(c,-1)

print("比他大的質數",a,b)
print("比他大的質數",c,d)

