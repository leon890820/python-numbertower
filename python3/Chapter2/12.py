n=int(input())
for i in range(2*n):
    if i<n:
        print(' '*2*n,end='')
        print(' '*(2*n-i-1)+'/'+'  '*i+'\\'+' '*(2*n-i-1),end='')
        print(' '*2*n)
    elif i==2*n-1:
        print('/'+'--'*(n-1)+'\\',end='')
        print('/'+'--'*(2*n-1)+'\\',end='')
        print('/'+'--'*(n-1)+'\\')
    else:
        print(' '*(2*n-i-1)+'/'+'  '*(i-n)+'\\'+' '*(2*n-i-1),end='')
        print(' '*(2*n-i-1)+'/'+'  '*(i)+'\\'+' '*(2*n-i-1),end='')
        print(' '*(2*n-i-1)+'/'+'  '*(i-n)+'\\'+' '*(2*n-i-1))
