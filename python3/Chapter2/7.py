n=int(input())
for i in range(n):
   for k in range(2):
       for j in range(k,2*n-1):
           if i==j or i+j==2*(n-1):
               print((j+k*(n-1)*2+1)%10,end='')
           else:
               print(' ',end='')
   print()   
